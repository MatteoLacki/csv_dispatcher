import argparse
import pandas as pd
import importlib

from pprint import pprint

from csv_dispatcher.parser import df2kwds_iter2
import multiprocessing as mp

DEBUG = True

P = argparse.ArgumentParser(description='Run a python function with csv input.',
                            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
AA = P.add_argument

AA("foo", help="Name of the function to run.")
AA("input_csv", help="Path to the csv file with inputs. Column 'group' should contain values uniquely describing groups in which the software should be run.")
AA("--module",
    default="builtins",
    help="Name of the module to import the function from.")
AA("--grouping_columns",
    default=[],
    nargs="*",
    help="Name(s) of column(s) storing groups.")
AA("--no_scalars",
    action='store_false',
    dest='as_scalar',
    help='Treat all arguments as lists.')
AA("--cores",
    help="Number of calls to schedule.", 
    type=int, 
    default=1)
AA("--verbose",
    help="Be verbose.", 
    action='store_true')
AA("--dry",
    help="Only show parsed arguments.", 
    action='store_true')

args = P.parse_args()

inputs_df = pd.read_csv(args.input_csv, engine="python", sep=None).dropna(axis=1, how='all')
if args.verbose:
    print(f"Calling 'csv_dispatch' on {args.foo}")
    print(inputs_df)

foo_kwds_iter = df2kwds_iter2(inputs_df, args.grouping_columns, args.as_scalar)

module = importlib.import_module(args.module)
foo = getattr(module, args.foo)

if args.dry:
    print(f"The arguments for function '{foo}' are:")
    for x in foo_kwds_iter:
        pprint(x)
else:
    if args.cores == 1:
        for group, kwds in foo_kwds_iter:
            foo(**kwds)
    else:
        def foo_wrapped(group_kwds):
            group, kwds = group_kwds
            return foo(**kwds)
        with mp.Pool(args.cores) as pool:
            pool.map(foo_wrapped, foo_kwds_iter)
        

import argparse
import pandas as pd
import importlib

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
AA("--dry_run",
    action='store_true',
    help='Output only keywords.')

args = P.parse_args()

inputs_df = pd.read_csv(args.input_csv, engine="python", sep=None).dropna(axis=1, how='all')
foo_kwds_iter = df2kwds_iter2(inputs_df, args.grouping_columns, args.as_scalar)

module = importlib.import_module(args.module)
foo = getattr(module, args.foo)

def foo_wrapped(group_kwds):
    group, kwds = group_kwds
    return foo(**kwds)

if args.cores == 1:
    for group, kwds in foo_kwds_iter:
        if args.dry_run:
            print(kwds)
        else:
            print(foo(**kwds))
else:
    with mp.Pool(args.cores) as pool:
        pool.starmap(foo_wrapped, foo_kwds_iter)

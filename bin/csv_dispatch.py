import argparse
import pandas as pd
import importlib

from csv_dispatcher.csv_dispatcher import df_map

DEBUG = True

P = argparse.ArgumentParser(description='Run a python function with csv input.',
                            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

AA = P.add_argument

AA("foo", help="Name of the function to run.")
AA("input_csv", help="Path to the csv file with inputs. Column 'group' should contain values uniquely describing groups in which the software should be run.")
AA("--module",
    default="builtins",
    help="Name of the module to import the function from.")
AA("--list_columns",
    default=[""],
    nargs="*",
    help="Name(s) of column(s) that should be run as list arguments of'foo'.")
AA("--grouping_columns",
    default=["group"],
    nargs="*",
    help="Name(s) of column(s) storing groups.")
AA("--cores",
    help="Number of calls to schedule.", 
    type=int, 
    default=1)

args = P.parse_args()
inputs_df = pd.read_csv(args.input_csv)
module = importlib.import_module(args.module)
foo = getattr(module, args.foo)
df_map(foo, inputs_df, args.grouping_columns, args.list_columns)


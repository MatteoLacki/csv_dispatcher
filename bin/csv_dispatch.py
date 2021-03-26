import argparse
import pandas as pd
import importlib

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

inputs_csv = pd.read_csv(args.input_csv)
if DEBUG:
    from pprint import pprint
    print(inputs_csv)
    print(args.__dict__)

module = importlib.import_module(args.module)
foo = getattr(module, args.foo)
if DEBUG:
    print(module)
    print(foo)

all_columns = set(inputs_csv.columns)
columns_to_be_dropped = all_columns - set(args.list_columns) - set(args.grouping_columns)

for group, group_data in inputs_csv.groupby(args.grouping_columns):
    non_list_args = group_data[columns_to_be_dropped].drop_duplicates()
    assert len(non_list_args) == 1, "Some values repeat multiple times within a group but ain't a list argument to 'foo': fix the input!."
    kwds = {**non_list_args.to_dict(orient="records")[0],
            **{name:list(col) for name, col in group_data[args.list_columns].to_dict(orient="series").items()}}
    res = foo(**kwds)
    if DEBUG:
        print(res)
%load_ext autoreload
%autoreload 2

import pandas as pd
import functools

from csv_dispatcher.parser import df2kwds_iter, df2kwds_iter2


list_columns = ["object"]
grouping_columns = ["group"]
dataframe = pd.read_csv("test/pprint_test.csv")
list(df2kwds_iter(dataframe, list_columns, grouping_columns))
list(df2kwds_iter(dataframe))

foo_dataframe = pd.read_csv("test/foo_test.csv")
dict(df2kwds_iter(foo_dataframe, list_columns=['x','y','z'], grouping_columns=["group"]))
dict(df2kwds_iter(dataframe))

df = pd.read_csv("test/pprint_test_with_NAs.csv")
df
list(df2kwds_iter2(df))
list(df2kwds_iter2(df, grouping_columns="group"))
list(df2kwds_iter2(df, grouping_columns=["group","object"]))
list(df2kwds_iter2(df, grouping_columns="group", as_scalar=False))





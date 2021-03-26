# TODO: add some form of multiprocessing!

def df_map(foo, dataframe, grouping_columns=[], list_columns=[]):
    columns_to_be_dropped = set(dataframe.columns) - set(list_columns) - set(grouping_columns)
    for group, group_data in dataframe.groupby(grouping_columns):
        non_list_args = group_data[columns_to_be_dropped].drop_duplicates()
        assert len(non_list_args) == 1, "Some values repeat multiple times within a group but ain't a list argument to 'foo': fix the input!."
        kwds = {**non_list_args.to_dict(orient="records")[0],
                **{name:list(col) for name, col in group_data[list_columns].to_dict(orient="series").items()}}
        foo(**kwds)
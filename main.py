from dataframe_creator import DataFrameCreator


dataframe_creator = DataFrameCreator()

dataframes = dataframe_creator.create_dataframes_in_batch("tables")

for df in dataframes:
    print(df.head())

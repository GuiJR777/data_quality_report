import os
import pandas as pd


class DataFrameCreator:
    def create_dataframe_by_excel_file(self, file_path: str) -> pd.DataFrame:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        if not (file_path.endswith(".xlsx") or file_path.endswith(".xlsb")):
            raise ValueError(f"The file {file_path} is not an Excel file.")

        try:
            return pd.read_excel(file_path)
        except Exception as e:
            raise ValueError(
                f"An error occurred while reading the Excel file: {e}"
            )

    def create_dataframe_by_csv_file(self, file_path: str) -> pd.DataFrame:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        if not file_path.endswith(".csv"):
            raise ValueError(f"The file {file_path} is not a CSV file.")

        try:
            return pd.read_csv(file_path, encoding='latin1', delimiter=";")
        except Exception as e:
            raise ValueError(
                f"An error occurred while reading the CSV file: {e}"
            )

    def create_dataframes_in_batch(
        self, folder_path: str
    ) -> list[pd.DataFrame]:
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(
                f"The folder {folder_path} does not exist."
            )

        dataframes = []

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if file_path.endswith(".xlsx") or file_path.endswith(".xlsb"):
                    dataframes.append(
                        self.create_dataframe_by_excel_file(file_path)
                    )
                elif file_path.endswith(".csv"):
                    dataframes.append(
                        self.create_dataframe_by_csv_file(file_path)
                    )
                else:
                    print(f"Unsupported file type: {file_path}")
            except Exception as e:
                print(f"Failed to process file {file_path}: {e}")

        return dataframes

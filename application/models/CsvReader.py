from .TableHeader import TableHeader

import pandas as pd


class CsvReader(object):
    def __init__(self, csv_model=pd):
        # Using pandas.
        self.csv_model = csv_model

    def load_setting(self, csvfile_path):
        self.dataframe = self.csv_model.read_csv(
            filepath_or_buffer=csvfile_path,
            header=None,
            encoding='utf-8',
            sep=',',
            index_col=TableHeader.KEY.value,
            dtype={TableHeader.KEY.value: 'str'}
        )

    def get_title(self, key: str) -> str:
        return self.dataframe.loc[key, TableHeader.TITLE.value]

    def get_text(self, key: str) -> str:
        return self.dataframe.loc[key, TableHeader.TEXT.value]

    def get_url(self, key: str) -> str:
        return self.dataframe.loc[key, TableHeader.URL.value]

    def get_row(self, key: str) -> list:
        list_record = self.dataframe.loc[key].tolist()
        list_record.insert(0, key)
        return list_record

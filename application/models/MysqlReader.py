import mysql.connector
import pandas.io.sql as psql

from .TableHeader import TableHeader


class MysqlReader(object):
    def __init__(self, data_model=psql, mysql_model=mysql.connector):
        # Using pandas.
        self.data_model = data_model
        self.mysql_model = mysql_model

    def load_setting(self, mysql_addr, mysql_port, db, table, user, password):
        # MySQLへ接続
        conn = self.mysql_model.connect(
            host=mysql_addr,
            port=mysql_port,
            db=db,
            user=user,
            password=password
        )
        # カラムを選択するならクエリを変更するのではなく、
        # read_sqlの引数のcolumnsにlist型を入れる。
        query = 'SELECT * FROM %s' % table
        self.dataframe = self.data_model.read_sql(
            sql=query,
            con=conn,
        )
        # dataframe上のカラムをTableHeaderに書き換えます。
        self.dataframe.columns = [i.value for i in TableHeader]
        # dataframe上のKEYをTableHeaderに書き換えます。
        self.dataframe.set_index(TableHeader.KEY.value, inplace=True)

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

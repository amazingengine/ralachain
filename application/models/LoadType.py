from enum import Enum


class LoadType(Enum):
    # 小文字と記号で記載するようにする。
    # 許容する文字列が複数あるならばそれぞれ別要素に記載する。
    CSV = ['csv']
    MYSQL = ['mysql', 'my-sql', 'my_sql']
    REDIS = ['redis']

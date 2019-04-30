from enum import IntEnum

import redis

from .TableHeader import TableHeader


class RedisReader(object):
    @staticmethod
    def sort_table_header(dict_key_val: dict) -> list:
        # TableHeader.list_str_headers()の順番通りにリスト化する。
        return [dict_key_val[header]
                for header in TableHeader.list_str_headers()]

    def __init__(self, redis_model=redis):
        self.redis_model = redis_model

    def load_setting(self, redis_addr, redis_port, password=None, db=0):
        conn_pool = self.redis_model.ConnectionPool(
            host=redis_addr,
            port=redis_port,
            db=db,
            password=password,
            encoding='utf-8',
            decode_responses=True
        )
        self.redis = self.redis_model.Redis(connection_pool=conn_pool)

    def get_title(self, key: str) -> str:
        return self.redis.hget(key, TableHeader.TITLE.value)

    def get_text(self, key: str) -> str:
        return self.redis.hget(key, TableHeader.TEXT.value)

    def get_url(self, key: str) -> str:
        return self.redis.hget(key, TableHeader.URL.value)

    def get_row(self, key):
        dict_key_val = self.redis.hgetall(key)
        # KEYがdict_key_valの辞書に存在しないので、挿入する。
        dict_key_val[str(TableHeader.KEY.value)] = key
        return RedisReader.sort_table_header(dict_key_val)

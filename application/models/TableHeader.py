from enum import IntEnum, auto


class TableHeader(IntEnum):
    # Datatableのタイトルカラムを数字にする。
    # auto()は1から連番で振られる。
    KEY = 0
    TITLE = auto()
    TEXT = auto()
    URL = auto()

    @classmethod
    def list_str_headers(cls) -> list:
        # タイトルカラムの整数を文字列にしてリストで出力します。
        return [str(i.value) for i in cls]

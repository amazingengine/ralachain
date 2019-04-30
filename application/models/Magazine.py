from enum import IntEnum, auto
from models.LoadType import LoadType


class Magazine(IntEnum):
    CSV = auto()
    MYSQL = auto()
    REDIS = auto()

    @staticmethod
    def select_magazine(load_type):
        if load_type in LoadType.CSV.value:
            return Magazine.CSV
        elif load_type in LoadType.MYSQL.value:
            return Magazine.MYSQL
        elif load_type in LoadType.REDIS.value:
            return Magazine.REDIS
        else:
            raise ValueError('You have selected a mode that does not exist.')

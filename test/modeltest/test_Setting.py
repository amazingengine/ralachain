import pytest
from models.Setting import Setting

CSV_INIFILE_PATH = '../test/mocks/csv_mode.ini'
REDIS_INIFILE_PATH = '../test/mocks/redis_mode.ini'
MYSQL_INIFILE_PATH = '../test/mocks/mysql_mode.ini'


@pytest.fixture()
def setting():
    # インスタンスを作成
    setting = Setting()
    return setting


@pytest.fixture()
def csv_settings():
    csv_settings = {
        'addr_or_hostname': None,
        'database': None,
        'debug_mode_is': None,
        'multibyte_mode_is': False,
        'password': None,
        'port': None,
        'tablename': None,
        'username': None,
        'engine': 1,
        'file': '../test/mocks/testdatas.csv',
    }
    return csv_settings


@pytest.fixture()
def redis_settings():
    redis_settings = {
        'debug_mode_is': None,
        'engine': 3,
        'file': None,
        'addr_or_hostname': '127.0.0.1',
        'port': '6379',
        'database': '0',
        'username': None,
        'password': 'None',
        'tablename': None,
        'multibyte_mode_is': False
    }
    return redis_settings


@pytest.fixture()
def mysql_settings():
    mysql_settings = {
        'debug_mode_is': None,
        'engine': 2,
        'file': None,
        'addr_or_hostname': '127.0.0.1',
        'port': '3306',
        'database': 'database',
        'username': 'root',
        'password': 'secret',
        'tablename': 'testdatas',
        'multibyte_mode_is': False
    }
    return mysql_settings


def test_csv_setting_prams(csv_settings):
    setting = Setting()
    setting.load_inifile(CSV_INIFILE_PATH)
    assert setting.__dict__ == csv_settings


def test_redis_setting_prams(redis_settings):
    setting = Setting()
    setting.load_inifile(REDIS_INIFILE_PATH)
    assert setting.__dict__ == redis_settings


def test_mysql_setting_prams(mysql_settings):
    setting = Setting()
    setting.load_inifile(MYSQL_INIFILE_PATH)
    assert setting.__dict__ == mysql_settings

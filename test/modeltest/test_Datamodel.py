import pytest

from models.Datamodel import Datamodel
from models.CsvReader import CsvReader
from models.Setting import Setting

CSV_INIFILE_PATH = '../test/mocks/csv_mode.ini'


@pytest.fixture()
def setting():
    # インスタンスを作成
    setting = Setting()
    return setting


def test_init_datamodel(setting):
    # インスタンスを作成
    data_model = Datamodel()
    setting.load_inifile(CSV_INIFILE_PATH)
    data_model.initting(setting)
    assert isinstance(data_model.magazine, CsvReader)

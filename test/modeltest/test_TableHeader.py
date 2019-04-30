from models.TableHeader import TableHeader


def test_datatable_columns():
    assert TableHeader.KEY == 0
    assert TableHeader.TITLE == 1
    assert TableHeader.TEXT == 2
    assert TableHeader.URL == 3


def test_list_str_nums():
    assert ['0', '1', '2', '3'] == TableHeader.list_str_headers()

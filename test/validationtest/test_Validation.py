import pytest
from validations.Validation import Validation


@pytest.fixture()
def validation():
    # インスタンスを作成
    validation = Validation()
    return validation


def test_urlkey(validation):
    assert 'key' == validation.urlvalue('key')
    assert 'hogehoge0123' == validation.urlvalue('hogehoge0123')
    assert '+' == validation.urlvalue('+')
    assert '_' == validation.urlvalue('_')
    assert 'ほげほげ' == validation.urlvalue('ほげほげ')

    with pytest.raises(ValueError):
        validation.urlvalue('-')
    with pytest.raises(ValueError):
        validation.urlvalue('/')
    with pytest.raises(ValueError):
        validation.urlvalue('?')
    with pytest.raises(ValueError):
        validation.urlvalue('&')
    with pytest.raises(ValueError):
        validation.urlvalue(' ')


def test_multi_byte(validation):
    assert 'aiueo' == validation.multi_byte('aiueo')
    assert 'UHOUHO' == validation.multi_byte('UHOUHO')
    assert 'DragonInstall' == validation.multi_byte('DragonInstall')
    assert '01' == validation.multi_byte('01')
    assert 'Abyssinian03' == validation.multi_byte('Abyssinian03')
    with pytest.raises(ValueError):
        validation.multi_byte('あいうえお')
    with pytest.raises(ValueError):
        validation.multi_byte('うほうほ')
    with pytest.raises(ValueError):
        validation.multi_byte('ドラゴンインストール')
    with pytest.raises(ValueError):
        validation.multi_byte('０１')
    with pytest.raises(ValueError):
        validation.multi_byte('アビシニアン０３')

import os

import pytest

from models.TableHeader import TableHeader
from models.MysqlReader import MysqlReader


@pytest.fixture()
def mysql_reader():
    # インスタンスを作成
    mysql_reader = MysqlReader()
    return mysql_reader


@pytest.fixture()
def setuped_mysql_reader(mysql_reader):
    # インスタンスを作成
    mysql_reader.load_setting(
        mysql_addr=os.getenv('MYSQL_HOSTNAME'),
        mysql_port=3306,
        db=os.getenv('MYSQL_DATABASE'),
        table='testdatas',
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'))

    return mysql_reader


def test_load_setting(mysql_reader):
    mysql_reader.load_setting(
        mysql_addr=os.getenv('MYSQL_HOSTNAME'),
        mysql_port=3306,
        db=os.getenv('MYSQL_DATABASE'),
        table='testdatas',
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'))


def test_get_title(setuped_mysql_reader):
    # 本文が長すぎるので先頭30文字まででテスト
    assert 'アーマードコア' == setuped_mysql_reader.get_title(key='hoge')
    assert 'バトルフィールド' == setuped_mysql_reader.get_title(key='fuga')
    assert 'CLLANAD' == setuped_mysql_reader.get_title(key='piyo')


def test_get_text(setuped_mysql_reader):
    # 本文が長すぎるので先頭30文字まででテスト
    assert '大破壊と呼ばれる全面戦争によって国家や政府は消滅した世界。生' == setuped_mysql_reader.get_text(
        key='hoge')[:30]
    assert '2002年発売の『バトルフィールド1942』より始まった、架' == setuped_mysql_reader.get_text(
        key='fuga')[:30]
    assert 'Keyが制作した3作目の恋愛アドベンチャーゲーム。このページ' == setuped_mysql_reader.get_text(
        key='piyo')[:30]


def test_get_url(setuped_mysql_reader):
    assert 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%BC%E3%83%9E%E3%83%BC%E3%83%89%E3%83%BB%E3%82%B3%E3%82%A2' == setuped_mysql_reader.get_url(
        key='hoge')
    assert 'https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%88%E3%83%AB%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%BC%E3%83%A0)' == setuped_mysql_reader.get_url(
        key='fuga')
    assert 'https://ja.wikipedia.org/wiki/CLANNAD_(%E3%82%B2%E3%83%BC%E3%83%A0)' == setuped_mysql_reader.get_url(
        key='piyo')


def test_get_row(setuped_mysql_reader):
    assert ['hoge', 'アーマードコア', '大破壊と呼ばれる全面戦争によって国家や政府は消滅した世界。生き延びた人類は地下都市へと移り住み、地上への復帰を目的とした企業連合体のもと、百年計画が進められる。計画が進展する中、巨大企業間の抗争が激化。それに伴い、多額の報酬と引き換えに企業に雇われ、立案された作戦に身を投じていく主人公を描いた話。アーマード・コアという人型機動兵器の操縦者であるレイヴンと呼ばれる傭兵、その中の1人が主人公という設定です。この初代作から既にシリーズの原型がほぼ完成されています。一般的なスーパーロボットアクションのカッコイイとは違い、どこか冷めた雰囲気のする世界観です。', 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%BC%E3%83%9E%E3%83%BC%E3%83%89%E3%83%BB%E3%82%B3%E3%82%A2'] == setuped_mysql_reader.get_row(
        key='hoge')
    assert ['fuga', 'バトルフィールド', '2002年発売の『バトルフィールド1942』より始まった、架空の戦争をテーマにしたゲームシリーズ。ゲームシステムは、チーム制のファーストパーソン・シューティングゲーム（FPS、一人称視点シュ-ティングゲーム）である。開発はスウェーデンのゲームソフトメーカーであるディジタル・イリュージョンズ・クリエイティブ・エンタテインメント（Digital Illusions Creative Entertainment、以下DICE）、販売はエレクトロニック・アーツが行っている。ウィンドウズをはじめ、マッキントッシュや各種コンシューマーゲーム機でも発売されている。', 'https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%88%E3%83%AB%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%BC%E3%83%A0)'] == setuped_mysql_reader.get_row(
        key='fuga')
    assert ['piyo', 'CLLANAD', 'Keyが制作した3作目の恋愛アドベンチャーゲーム。このページではこのゲームを原作として、メディアミックス的展開がなされたアニメやコミックなどの作品群についても解説する。', 'https://ja.wikipedia.org/wiki/CLANNAD_(%E3%82%B2%E3%83%BC%E3%83%A0)'] == setuped_mysql_reader.get_row(
        key='piyo')
    assert '大破壊と呼ばれる全面戦争によって国家や政府は消滅した世界。生き延びた人類は地下都市へと移り住み、地上への復帰を目的とした企業連合体のもと、百年計画が進められる。計画が進展する中、巨大企業間の抗争が激化。それに伴い、多額の報酬と引き換えに企業に雇われ、立案された作戦に身を投じていく主人公を描いた話。アーマード・コアという人型機動兵器の操縦者であるレイヴンと呼ばれる傭兵、その中の1人が主人公という設定です。この初代作から既にシリーズの原型がほぼ完成されています。一般的なスーパーロボットアクションのカッコイイとは違い、どこか冷めた雰囲気のする世界観です。' == setuped_mysql_reader.get_row(
        key='hoge')[TableHeader.TEXT.value]
    assert 'fuga' == setuped_mysql_reader.get_row(key='fuga')[
        TableHeader.KEY.value]
    assert 'CLLANAD' == setuped_mysql_reader.get_row(
        key='piyo')[TableHeader.TITLE.value]

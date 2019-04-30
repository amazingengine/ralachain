import pytest

from models.TableHeader import TableHeader
from models.CsvReader import CsvReader


@pytest.fixture()
def csv_reader():
    # インスタンスを作成
    csv_reader = CsvReader()
    return csv_reader


def test_load_setting(csv_reader):
    csv_reader.load_setting(
        csvfile_path='../test/mocks/testdatas.csv')


def test_get_title(csv_reader):
    # このModeltestのディレクリ内にあるtestdatas.csvを読み込みます。
    csv_reader.load_setting(
        csvfile_path='../test/mocks/testdatas.csv')
    # 本文が長すぎるので先頭30文字まででテスト
    assert 'アーマードコア' == csv_reader.get_title(key='honda')
    assert 'バトルフィールド' == csv_reader.get_title(key='yamaha')
    assert 'CLLANAD' == csv_reader.get_title(key='suzuki')


def test_get_text(csv_reader):
    # このModeltestのディレクリ内にあるtestdatas.csvを読み込みます。
    csv_reader.load_setting(
        csvfile_path='../test/mocks/testdatas.csv')
    # 本文が長すぎるので先頭30文字まででテスト
    assert '大破壊と呼ばれる全面戦争によって国家や政府は消滅した世界。生' == csv_reader.get_text(
        key='honda')[:30]
    assert '2002年発売の『バトルフィールド1942』より始まった、架' == csv_reader.get_text(
        key='yamaha')[:30]
    assert 'Keyが制作した3作目の恋愛アドベンチャーゲーム。このページ' == csv_reader.get_text(
        key='suzuki')[:30]


def test_get_url(csv_reader):
    # このModeltestのディレクリ内にあるtestdatas.csvを読み込みます。
    csv_reader.load_setting(
        csvfile_path='../test/mocks/testdatas.csv')

    assert 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%BC%E3%83%9E%E3%83%BC%E3%83%89%E3%83%BB%E3%82%B3%E3%82%A2' == csv_reader.get_url(
        key='honda')
    assert 'https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%88%E3%83%AB%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%BC%E3%83%A0)' == csv_reader.get_url(
        key='yamaha')
    assert 'https://ja.wikipedia.org/wiki/CLANNAD_(%E3%82%B2%E3%83%BC%E3%83%A0)' == csv_reader.get_url(
        key='suzuki')


def test_get_row(csv_reader):
    # このModeltestのディレクリ内にあるtestdatas.csvを読み込みます。
    csv_reader.load_setting(
        csvfile_path='../test/mocks/testdatas.csv')

    assert ['honda', 'アーマードコア', '大破壊と呼ばれる全面戦争によって国家や政府は消滅した世界。生き延びた人類は地下都市へと移り住み、地上への復帰を目的とした企業連合体のもと、百年計画が進められる。計画が進展する中、巨大企業間の抗争が激化。それに伴い、多額の報酬と引き換えに企業に雇われ、立案された作戦に身を投じていく主人公を描いた話。アーマード・コアという人型機動兵器の操縦者であるレイヴンと呼ばれる傭兵、その中の1人が主人公という設定です。この初代作から既にシリーズの原型がほぼ完成されています。一般的なスーパーロボットアクションのカッコイイとは違い、どこか冷めた雰囲気のする世界観です。', 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%BC%E3%83%9E%E3%83%BC%E3%83%89%E3%83%BB%E3%82%B3%E3%82%A2'] == csv_reader.get_row(
        key='honda')
    assert ['yamaha', 'バトルフィールド', '2002年発売の『バトルフィールド1942』より始まった、架空の戦争をテーマにしたゲームシリーズ。ゲームシステムは、チーム制のファーストパーソン・シューティングゲーム（FPS、一人称視点シュ-ティングゲーム）である。開発はスウェーデンのゲームソフトメーカーであるディジタル・イリュージョンズ・クリエイティブ・エンタテインメント（Digital Illusions Creative Entertainment、以下DICE）、販売はエレクトロニック・アーツが行っている。ウィンドウズをはじめ、マッキントッシュや各種コンシューマーゲーム機でも発売されている。', 'https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%88%E3%83%AB%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89_(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC%E3%82%B2%E3%83%BC%E3%83%A0)'] == csv_reader.get_row(
        key='yamaha')
    assert ['suzuki', 'CLLANAD', 'Keyが制作した3作目の恋愛アドベンチャーゲーム。このページではこのゲームを原作として、メディアミックス的展開がなされたアニメやコミックなどの作品群についても解説する。', 'https://ja.wikipedia.org/wiki/CLANNAD_(%E3%82%B2%E3%83%BC%E3%83%A0)'] == csv_reader.get_row(
        key='suzuki')
    assert '大破壊と呼ばれる全面戦争によって国家や政府は消滅した世界。生き延びた人類は地下都市へと移り住み、地上への復帰を目的とした企業連合体のもと、百年計画が進められる。計画が進展する中、巨大企業間の抗争が激化。それに伴い、多額の報酬と引き換えに企業に雇われ、立案された作戦に身を投じていく主人公を描いた話。アーマード・コアという人型機動兵器の操縦者であるレイヴンと呼ばれる傭兵、その中の1人が主人公という設定です。この初代作から既にシリーズの原型がほぼ完成されています。一般的なスーパーロボットアクションのカッコイイとは違い、どこか冷めた雰囲気のする世界観です。' == csv_reader.get_row(
        key='honda')[TableHeader.TEXT.value]
    assert 'honda' == csv_reader.get_row(key='honda')[TableHeader.KEY.value]
    assert 'CLLANAD' == csv_reader.get_row(
        key='suzuki')[TableHeader.TITLE.value]

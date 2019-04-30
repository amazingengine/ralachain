import configparser

from models.Magazine import Magazine


class Setting(object):
    def __init__(self):
        # settings
        self.debug_mode_is = True
        self.engine = None
        self.file = None
        self.addr_or_hostname = None
        self.port = None
        self.database = None
        self.username = None
        self.password = None
        self.tablename = None
        # options
        self.multibyte_mode_is = False

    def load_inifile(self, ini_file, encode='utf-8'):
        # iniファイルを読み込むためのconfParserのインスタンス作成等
        conf = configparser.ConfigParser(allow_no_value=True)
        conf.read(ini_file, encode)
        # debug_mode確認
        self.debug_setting(conf['settings'].getboolean('debug'))
        # main情報読み込み
        self.main_setting(conf['settings'])
        # options情報読み込み。
        try:
            self.option_setting(conf['options'])
        except KeyError:
            # Optionの設定がなければpass
            pass

    def debug_setting(self, conf_debug: bool):
        self.debug_mode_is = conf_debug

    def main_setting(self, conf_settings):
        # モードの表記ゆれ対策「mysql」[My-SQL]など
        load_type = conf_settings.get('engine').lower()
        self.engine = Magazine.select_magazine(load_type)
        # 存在しない値をgetした場合はNoneになります。
        self.file = conf_settings.get('file')
        self.addr_or_hostname = conf_settings.get('ipaddr_or_hostname')
        self.port = conf_settings.get('port')
        self.username = conf_settings.get('username')
        self.password = conf_settings.get('password')
        self.database = conf_settings.get('db')
        self.tablename = conf_settings.get('tablename')

    def option_setting(self, conf_option):
        self.multibyte_mode_is = conf_option.getboolean('key_multibyte')

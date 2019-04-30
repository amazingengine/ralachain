'''
Flaskを実行するプログラム。
factory_appから設定を引き継いで実行されます。
'''
import sys

from flask import Flask, render_template

from singletons.datamodel import datamodel
from singletons.setting import setting
from validations.Validation import Validation

# コマンドライン引数の取得
ini_file = sys.argv[1]
setting.load_inifile(ini_file)
# シングルトンの初期化
datamodel.initting(setting)
validation = Validation()


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template(
        'index.html',
        hello='hello'
    )


@app.route('/<string:key>')
def argment(key: str):
    validation.urlvalue(key)
    if not setting.multibyte_mode_is:
        validation.multi_byte(key)
    return datamodel.magazine.get_text(key)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

'''
pytestは初めのこのconftest.pyを読み込みます。
ここではテストしたいファイルが置いてあるパスを
psytestを行う場所に指定します。
モジュールなども指定したパスを起点に行います。
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + '/../application/'))
# https://www.magata.net/memo/index.php?pytest%C6%FE%CC%E7#y2046859

from models.Magazine import Magazine
from models.CsvReader import CsvReader
from models.MysqlReader import MysqlReader
from models.RedisReader import RedisReader


class Datamodel(object):

    def initting(self,  setting):
        if setting.engine == Magazine.CSV:
            self.magazine = CsvReader()
            self.magazine.load_setting(
                csvfile_path=setting.file
            )
        elif setting.engine == Magazine.MYSQL:
            self.magazine = MysqlReader()
            self.magazine.load_setting(
                mysql_addr=setting.addr_or_hostname,
                mysql_port=setting.port,
                db=setting.database,
                table=setting.tablename,
                user=setting.username,
                password=setting.password
            )
        elif setting.engine == Magazine.REDIS:
            if setting.password == 'None':
                password = None
            else:
                password = setting.password
            self.magazine = RedisReader()
            self.magazine.load_setting(
                redis_addr=setting.addr_or_hostname,
                redis_port=setting.port,
                password=password,
                db=setting.database
            )

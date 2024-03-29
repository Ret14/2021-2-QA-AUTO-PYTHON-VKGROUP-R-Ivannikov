import pytest
from python_scripts.ultimate_script import *
from mysql_orm.client import MysqlORMClient
from utils.builder_orm import MysqlORMBuilder


class MysqlBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client, fill_tables, data_dict):
        self.mysql: MysqlORMClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)
        self.data_dict = data_dict

    @pytest.fixture(scope='session')
    def fill_tables(self, mysql_orm_client, data_dict):
        MysqlORMBuilder(mysql_orm_client).make_dbs(data_dict)

    @pytest.fixture(scope='session')
    def data_dict(self):
        return get_data()

    def get_table(self, model):
        return self.mysql.session.query(model).all()

import pytest
from ultimate_script import *
from models.model import *
from mysql_orm.client import MysqlORMClient
from utils.builder_orm import MysqlORMBuilder


class MysqlBase:

    # is called from setup fixture on every test. test can override this method for its custom data prepare
    def prepare(self):
        self.mysql_builder.make_dbs(get_data())

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client, fill_tables):
        self.mysql: MysqlORMClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)
        # self.mysql_builder.make_dbs(get_data())
        # self.prepare()

    # @pytest.fixture(scope='session')
    # def fill_tables(self):
    #     self.mysql_builder.make_dbs(get_data())
    # def get_students(self, prepod_id=None):
    #     self.mysql.session.commit()  # need to expire current models and get updated data from MySQL
    #     students = self.mysql.session.query(Student)
    #
    #     # additionally filter by prepod_id
    #     if prepod_id is not None:
    #         students = students.filter_by(prepod_id=prepod_id)
    #     return students.all()

    # def get_requests_amount(self):
    #     return self.mysql.session.query(RequestsAmount).all()
    #
    # def get_top10_most_frequent(self):

    def get_table(self, model):
        return self.mysql.session.query(model).all()

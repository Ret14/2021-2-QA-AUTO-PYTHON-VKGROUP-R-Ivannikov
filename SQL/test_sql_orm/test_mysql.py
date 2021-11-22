from sqlalchemy import func

from models.model import *
from test_sql_orm.base import MysqlBase


class TestTableElementsAmount(MysqlBase):

    def test_requests_amount(self):
        assert len(self.get_table(RequestsAmount)) == 1

    def test_requests_by_type(self):
        assert len(self.get_table(RequestsByType)) == 4

    def test_top10_most_frequent(self):
        assert len(self.get_table(Top10MostFrequent)) == 10

    def test_top5_5xx_err(self):
        assert len(self.get_table(Top5Err5xx)) == 5

    def test_top5_4xx_err(self):
        assert len(self.get_table(Top5Err4xx)) == 5

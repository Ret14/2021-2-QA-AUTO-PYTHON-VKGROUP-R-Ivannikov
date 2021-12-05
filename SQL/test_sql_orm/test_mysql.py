from models.model import *
from base import MysqlBase


class TestTableElementsAmount(MysqlBase):

    def test_requests_amount(self):
        assert len(self.get_table(RequestsAmount)) == 1

    def test_requests_by_type(self):
        assert len(self.get_table(RequestsByType)) == len(self.data_dict['requests_by_type'])

    def test_top10_most_frequent(self):
        assert len(self.get_table(Top10MostFrequent)) == len(self.data_dict['top10_most_frequent'])

    def test_top5_5xx_err(self):
        assert len(self.get_table(Top5Err5xx)) == len(self.data_dict['top5_5xx_err'])

    def test_top5_4xx_err(self):
        assert len(self.get_table(Top5Err4xx)) == len(self.data_dict['top5_4xx_err'])

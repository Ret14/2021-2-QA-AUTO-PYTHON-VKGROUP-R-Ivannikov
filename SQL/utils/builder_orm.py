from faker import Faker

from models.model import *

# fake = Faker()


class MysqlORMBuilder:

    def __init__(self, client):
        self.client = client

    # def create_prepod(self, name=None, surname=None, start_teaching=None):
    #     if name is None:
    #         name = fake.first_name()
    #
    #     if surname is None:
    #         surname = fake.last_name()
    #
    #     if start_teaching is None:
    #         start_teaching = fake.date()
    #
    #     prepod = Prepod(
    #         name=name,
    #         surname=surname,
    #         start_teaching=start_teaching
    #     )
    #     prepod.name = 'Ilya'
    #
    #     self.client.session.add(prepod)
    #     self.client.session.commit()
    #     return prepod
    #
    # def create_student(self, name=None, prepod_id=None):
    #     if prepod_id is None:
    #         prepod_id = self.create_prepod().id
    #
    #     if name is None:
    #         name = fake.first_name()
    #
    #     student = Student(
    #         name=name,
    #         prepod_id=prepod_id
    #     )
    #     self.client.session.add(student)
    #     self.client.session.commit()
    #     return student

    def make_dbs(self, datadict: dict):
        self.add_requests_amount(datadict['requests_amount'])

        for method in datadict['requests_by_type']:
            self.add_requests_by_type(method=method,
            amount=datadict['requests_by_type'][method])

        for url in datadict['top10_most_frequent']:
            self.add_top10_most_frequent(url=url,
            amount=datadict['top10_most_frequent'][url])

        for ip in datadict['top5_5xx_err']:
            self.add_top5_5xx(ip=ip,
            amount=datadict['top5_5xx_err'][ip])

        for elem in datadict['top5_4xx_err']:
            self.add_top5_4xx(
            Url=elem[0], Status_code=elem[1],
            Url_size=elem[2], IP=elem[3])



    def add_requests_amount(self, amount=None):
        requests_number = RequestsAmount(
            Requests_amount = amount
        )

        self.client.session.add(requests_number)
        self.client.session.commit()
        return requests_number

    def add_top10_most_frequent(self, url=None, amount=None):
        top_10 = Top10MostFrequent(
            Url = url
            Requests_amount = amount
        )

        self.client.session.add(top_10)
        self.client.session.commit()
        return top_10

    def add_top5_5xx(self, ip=None, amount=None):
        top_5 = Top5Err5xx(
            IP = ip
            Requests_amount = amount
        )

        self.client.session.add(top_5)
        self.client.session.commit()
        return top_5

    def add_requests_by_type(self, method=None, amount=None):
        top_methods = RequestsByType(
            Request_method = method
            RequestsAmount = amount
        )

        self.client.session.add(top_methods)
        self.client.session.commit()
        return top_methods

    def add_top5_4xx(self, Url=None, Status_code=None, Url_size=None, IP=None):
        top_5 = Top5Err4xx(
            Url = Url
            Status_code = Status_code
            Url_size = Url_size
            IP = IP
        )

        self.client.session.add(top_5)
        self.client.session.commit()
        return top_5

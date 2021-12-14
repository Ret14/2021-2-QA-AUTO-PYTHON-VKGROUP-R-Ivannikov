import pytest
from faker import Faker
import settings


class BaseCase:

    fake = Faker()
    host = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'

    @pytest.fixture(scope='function')
    def user(self):
        return {'name': self.fake.first_name(), 'surname': self.fake.last_name()}

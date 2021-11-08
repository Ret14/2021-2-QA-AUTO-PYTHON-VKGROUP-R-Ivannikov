import pytest


class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, logger):
        self.api_client = api_client
        self.logger = logger
        self.api_client.target_authorize()

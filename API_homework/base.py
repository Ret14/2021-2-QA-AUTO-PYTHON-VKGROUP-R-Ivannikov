import pytest


class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, logger):
        self.api_client = api_client
        self.logger = logger
        self.api_client.target_authorize()

    @pytest.fixture(scope='function')
    def camp_delete(self, api_client):
        yield
        api_client.camp_discard()
        assert not api_client.camp_exist_check()

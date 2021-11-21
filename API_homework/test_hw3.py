import pytest
import logging
from base import ApiBase

logger = logging.getLogger('test')


@pytest.mark.API
class TestSegments(ApiBase):

    def test_segment_create(self):
        self.api_client.post_segment()
        assert self.api_client.segment_exist_check()
        self.api_client.delete_segment()

    def test_segment_delete(self):
        self.test_segment_create()
        assert not self.api_client.segment_exist_check()


@pytest.mark.usefixtures('camp_delete')
@pytest.mark.API
class TestCampaign(ApiBase):
    def test_camp_creation(self, prepare_image):
        self.api_client.post_camp(self.api_client.post_image(prepare_image))
        assert self.api_client.camp_existence_check()

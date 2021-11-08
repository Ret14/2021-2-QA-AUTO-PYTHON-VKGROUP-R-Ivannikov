import pytest

from base import ApiBase


@pytest.mark.API
class TestSegments(ApiBase):

    def test_segment_create(self):
        self.api_client.post_segment()
        self.api_client.delete_segment()

    def test_segment_discard(self):
        self.test_segment_create()





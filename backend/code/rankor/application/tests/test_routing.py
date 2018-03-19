from unittest.mock import MagicMock
from unittest.mock import patch

from pytest import fixture

from rankor.application.routing import RankorRouting


class TestRankorRouting(object):
    @fixture
    def madd(self):
        with patch.object(RankorRouting, 'add') as mock:
            yield mock

    @fixture
    def mpyramid(self):
        return MagicMock()

    def test_routing(self, madd, mpyramid):
        """
        This is syntax check of the routing.
        """
        RankorRouting(mpyramid).make()

        madd.assert_called()

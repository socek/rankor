from unittest.mock import MagicMock
from unittest.mock import patch

from pytest import fixture

from mypet.application.routing import MypetRouting


class TestMypetRouting(object):
    @fixture
    def madd(self):
        with patch.object(MypetRouting, 'add') as mock:
            yield mock

    @fixture
    def mpyramid(self):
        return MagicMock()

    def test_routing(self, madd, mpyramid):
        """
        This is syntax check of the routing.
        """
        MypetRouting(mpyramid).make()

        madd.assert_called()

from unittest.mock import MagicMock
from unittest.mock import patch

from pytest import fixture

from cashflow.application.routing import CashflowRouting


class TestCashflowRouting(object):
    @fixture
    def madd(self):
        with patch.object(CashflowRouting, 'add') as mock:
            yield mock

    @fixture
    def mpyramid(self):
        return MagicMock()

    def test_routing(self, madd, mpyramid):
        """
        This is syntax check of the routing.
        """
        CashflowRouting(mpyramid).make()

        madd.assert_called()

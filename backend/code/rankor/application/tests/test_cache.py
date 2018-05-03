from unittest.mock import MagicMock

from rankor.application.cache import cache_per_request


class SampleView(object):
    def __init__(self):
        self.request = MagicMock()
        self.request._cache = {}
        self.counter = 0

    @cache_per_request('something')
    def get_something(self):
        self.counter += 1
        return self.counter


def test_cache_per_request():
    """
    cache_per_request should run cached method only once per request
    """
    view = SampleView()

    assert view.get_something() == 1
    assert view.get_something() == 1

    assert view.counter == 1

from collections import namedtuple

from sapp.plugins.settings import PrefixedStringsDict

Settings = namedtuple('Settings', ['config', 'paths'])


def default():
    config = {}
    paths = PrefixedStringsDict('/code/')
    return config, paths


def pyramid():
    config, paths = default()
    return Settings(config, paths)

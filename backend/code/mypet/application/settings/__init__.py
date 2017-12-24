from mypet.application.settings.default import default
from mypet.application.settings.pyramid import pyramid_specific


def pyramid():
    settings = default()
    pyramid_specific(settings)
    return settings


def command():
    return default()

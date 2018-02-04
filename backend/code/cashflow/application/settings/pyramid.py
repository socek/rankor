def pyramid_specific(settings):
    settings['pyramid.reload_templates'] = True
    settings['session_secret'] = 'this is not a secret'
    settings['secret'] = 'this is not a secret'

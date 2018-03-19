from pyramid.security import Allow
from pyramid.security import Everyone


class MainRoot(object):
    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
            (Allow, self.owner, 'edit'),
        ]

    def __init__(self, owner):
        self.owner = owner

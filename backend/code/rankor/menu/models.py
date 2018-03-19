class MenuElement(object):

    def __init__(self, name, text, url):
        self.name = name
        self.text = text
        self.url = url

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def get_url(self):
        return self.url

    def get_is_active(self):
        return False

    def serialize(self):
        return {
            'name': self.get_name(),
            'text': self.get_text(),
            'url': self.get_url(),
            'is_active': self.get_is_active(),
        }


class MenuGroup(object):

    def __init__(self, name=''):
        self.name = name
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def serialize(self):
        return {
            'name': self.name,
            'elements': [element.serialize() for element in self.elements]
        }


class Menu(object):

    def __init__(self, request):
        self.groups = []
        self.request = request
        self.make_menu()

    def add(self, *args, **kwargs):
        group = MenuGroup(*args, **kwargs)
        self.groups.append(group)
        return group

    def serialize(self):
        return [group.serialize() for group in self.groups]

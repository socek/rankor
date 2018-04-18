from functools import wraps


def cache_per_request(name):
    def wrapper(method):
        @wraps(method)
        def wrapped(self, *args, **kwargs):
            cache = getattr(self.request, '_cache', {})
            if name not in cache:
                cache[name] = method(self, *args, **kwargs)
                self.request._cache = cache
            return cache[name]

        return wrapped

    return wrapper

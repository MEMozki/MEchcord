def command(name=None):
    def decorator(func):
        func.__command__ = name or func.__name__
        return func
    return decorator
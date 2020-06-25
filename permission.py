from functools import wraps


def security(*ability):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if len(ability) > 0:
                return func(*args, **kwargs)
            return {"message": "You don't have permission"}

        return inner

    return wrapper

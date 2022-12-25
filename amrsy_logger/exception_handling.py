import pymongo
import time

_admisterable_exception = (pymongo.errors.AutoReconnect)

def retry(times=1000, exceptions=_admisterable_exception):
    def decorator(func):
        def newfn(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d' % (func, attempt, times)
                    )
                    attempt += 1
                    time.sleep(10)
                    print(
                        'retrying after sleep of 10 seconds'
                    )
            return func(*args, **kwargs)
        return newfn
    return decorator
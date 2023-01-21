import pymongo
import time

_admisterable_exception = (pymongo.errors.AutoReconnect, pymongo.errors.ServerSelectionTimeoutError, pymongo.errors.CursorNotFound, pymongo.errors.WriteConcernError)

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
                    time.sleep(2 * 60)
                    print(
                        'retrying after sleep of 10 seconds'
                    )
            return func(*args, **kwargs)
        return newfn
    return decorator

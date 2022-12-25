import time
import pymongo

def sample_run():
    raise pymongo.errors.AutoReconnect


from amrsy_logger import log_function

log_function(sample_run)

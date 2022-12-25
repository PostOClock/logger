from datetime import datetime
from .exception_handling import retry
from .db import (active_moudules_queue_connection, logs_queue_connection)


def record_acive_modules(data):
    data.pop("_id")
    query = {"module": data["module"]}
    data = {"$set": data}
    active_moudules_queue_connection.update_one(query, data, upsert=True)


def add_to_log(time_taken, module, system=None, type_c=None):
    insert_data = {
        "time_taken": round(time_taken, 2),
        "module": module,
        "insert_time": datetime.utcnow(),
    }

    if type_c == "system":
        insert_data["system"] = system
        insert_data["type"] = type_c

    logs_queue_connection.insert_one(insert_data)
    record_acive_modules(insert_data)


def time_function(function):
    start = datetime.now()
    function()
    end = datetime.now()
    time_taken = end - start
    time_taken = time_taken.total_seconds()
    time_taken = round(time_taken, 2)
    return time_taken

@retry()
def log_function(function, *args, **kwargs):
    module = function.__name__
    time_taken = time_function(function, *args, **kwargs)
    add_to_log(time_taken, module)

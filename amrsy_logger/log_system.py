import platform
import time

import psutil

from .functions import add_to_log

_LOG_SYSTEM_INTERVAL = 60


def get_system_info():
    return_data = {}
    return_data["platform"] = platform.node()

    memory = psutil.virtual_memory()

    return_data["memory"] = {"total": memory.total, "used_percent": memory.percent}

    return_data["cpu"] = {
        "cpu_count": psutil.cpu_count(),
        "used_percent": psutil.cpu_percent(5),
    }

    return return_data


def log_system_info():
    system_info = get_system_info()
    module = "system " + system_info["platform"]
    add_to_log(time_taken=0, module=module, system=system_info, type_c="system")


def run_log_system_info():
    while True:
        log_system_info()
        time.sleep(_LOG_SYSTEM_INTERVAL)

from datetime import datetime, timedelta

from database.connection import active_moudules_queue_connection


def system_print(entry, difference):
    system = entry["system"]
    print("--------------------------------------")
    print("platform :", system["platform"])
    print("time ago :", str(timedelta(seconds=difference)))
    print(
        "memory : total :",
        system["memory"]["total"],
        "used_percent :",
        system["memory"]["used_percent"],
    )
    print(
        "cpu : cpu_count :",
        system["cpu"]["cpu_count"],
        "used_percent :",
        system["cpu"]["used_percent"],
    )
    print("\n")


def normal_print(entry, difference):
    print("--------------------------------------")
    print(entry["module"])
    print("time ago :", str(timedelta(seconds=difference)))
    print("time taken :", entry["time_taken"])
    print("\n")
    pass


def report():
    query_data = list(active_moudules_queue_connection.find())

    print("modules report")

    for entry in query_data:
        utc_time_now = datetime.utcnow()
        difference = (utc_time_now - entry["insert_time"]).total_seconds()

        type_c = entry.get("type")

        if type_c == "system":
            continue
        else:
            normal_print(entry, difference)

    print("\n\n\n")
    print("system report")

    for entry in query_data:
        utc_time_now = datetime.utcnow()
        difference = (utc_time_now - entry["insert_time"]).total_seconds()

        type_c = entry.get("type")
        if type_c == "system":
            system_print(entry, difference)
        else:
            continue

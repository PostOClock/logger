from database import mongo_client


queue_db = mongo_client["queue"]

logs_queue_connection = queue_db["logs"]
active_moudules_queue_connection = queue_db["active-moudules"]

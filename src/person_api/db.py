"""
Database client module for interfacing with MongoDB.
"""
from flask import current_app, g
from werkzeug.local import LocalProxy
from pymongo import MongoClient, DESCENDING, ASCENDING

def get_db():
    """
    Configuration method to return a db instance
    """
    DB_URI = current_app.config["DB_URI"]
    DB_NAME = current_app.config["NS"]
    MAX_POOL_SIZE = current_app.config["MAX_POOL_SIZE"]
    WRITE_TIMEOUT = current_app.config["WRITE_TIMEOUT"]

    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = MongoClient(
            DB_URI, maxPoolSize=MAX_POOL_SIZE, waitQueueTimeoutMS=WRITE_TIMEOUT
        )[DB_NAME]
    return db

_DB = LocalProxy(get_db) # Use LocalProxy to read the global database object


def fetch_persons(per_page=100, sort_by='lname', last_id=None):
    if last_id:
        cursor = _DB["persons"].find({"_id": {"$gt": last_id}}).sort(sort_by, ASCENDING)
    else:
        cursor = _DB["persons"].find().sort(sort_by, ASCENDING)
    persons_data = list(cursor.limit(per_page))

    return (persons_data, persons_data[-1]["_id"])

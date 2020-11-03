import pytest
import mongoengine
from pymongo.database import Database
from person_api.db import fetch_persons, fetch_person
from pymongo.mongo_client import MongoClient
from flask_mongoengine import MongoEngine, current_mongoengine_instance, current_app


def test_connection(client):
    # Verify db settings passed to pymongo driver.
    connection = mongoengine.get_connection()
    mongo_engine_db = mongoengine.get_db()
    assert isinstance(mongo_engine_db, Database)
    assert isinstance(connection, MongoClient)
    assert mongo_engine_db.name == current_app.config["MONGODB_SETTINGS"]["db"]


def test_fetch_person(client):
    document = fetch_person("5f9c432f06f8bb3f8eba2e4b")[0]
    assert document is not None
    assert document.lname == "Teece"


def test_fetch_persons(client):
    count_per_page = 10
    rslt = fetch_persons(count_per_page)
    assert rslt.per_page == 10
    assert rslt.items[0]["lname"] == "Ales0"

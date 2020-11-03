import pytest
from pymongo import MongoClient
from person_api.db import fetch_persons

def test_fetch_persons(client):
    count_per_page = 10
    (rslt, last_id) = fetch_persons(count_per_page, 'lname')
    assert rslt[0]['lname'] == "Ales0"
    assert len(rslt) == count_per_page

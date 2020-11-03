"""
Service managing data for Person type
"""
from person_api.db import fetch_persons, fetch_person


def get_persons():
    persons = fetch_persons().items
    return persons


def get_person(id: str):
    return fetch_person(id)[0]

"""
Service managing data for Person type
"""
from person_api.db import (
    fetch_persons,
    fetch_person,
    save_person,
    fetch_person_revision,
    set_person_fields,
    delete_person,
)
from person_api.models.persons import Persons


def get_persons():
    persons = fetch_persons().items
    return persons


def get_person(id: str):
    try:
        person = fetch_person(id)[0]
    except Exception:
        return None
    return person


def get_person_revision(id: str, revision: int):
    return fetch_person_revision(id, revision)[0]


def new_person(fname: str, lname: str, mname: str, email: str, age: int):
    p = Persons(fname=fname, lname=lname, mname=mname, email=email, age=age)
    save_person(p)
    rslt = Persons.objects(fname=fname, lname=lname, email=email, age=age)
    return rslt[0]


def update_person_by_id(id: str, **kwargs):
    person = get_person(id)
    return set_person_fields(person, **kwargs)[0]


def remove_person_by_id(id: str):
    person = get_person(id)
    delete_person(person)

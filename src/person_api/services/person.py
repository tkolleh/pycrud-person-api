"""
Service managing data for Person type
"""
from person_api.models.person import Persons
from person_api.db import fetch_persons, fetch_person, save_person, set_person_fields


def get_persons():
    persons = fetch_persons().items
    return persons


def get_person(id: str):
    return fetch_person(id)[0]


def new_person(fname: str, lname: str, mname: str, email: str, age: int):
    p = Persons(fname=fname, lname=lname, mname=mname, email=email, age=age)
    save_person(p)

    rslt = Persons.objects(fname=fname, lname=lname, email=email, age=age)
    return rslt[0]


def update_person_by_id(id: str, **kwargs):
    person = get_person(id)
    set_person_fields(person, **kwargs)

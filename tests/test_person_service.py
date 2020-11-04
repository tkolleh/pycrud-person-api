import pytest
from person_api.services.person import (
    get_persons,
    get_person,
    new_person,
    update_person_by_id,
)
from person_api.models.persons import Persons


class TestPersons:
    empty = Persons()
    full = Persons(
        fname="Nala", lname="Lion", email="nl@cartoon.com", age=22, id="123abc"
    )

    def test_dunder_str(self):
        assert str(self.empty) != ""
        assert "Persons{" in str(self.empty)
        assert "mem_adr" in str(self.full) and self.full.id in str(self.full)

    def test_dunder_eq(self):
        assert self.empty != self.full
        self.full_dupe = self.full
        assert self.full_dupe == self.full


def test_get_persons(client):
    persons = get_persons()
    assert len(persons) >= 100


def test_get_person(client):
    person = get_person("5f9c432f06f8bb3f8eba2e4d")
    assert person is not None
    assert person.lname == "Aspel"


def test_new_person(client):
    jane_doe = new_person(
        fname="Jane", mname="", lname="Doe", email="jd@missing.com", age=33
    )
    assert jane_doe is not None
    assert jane_doe.fname == "Jane"

    jane_doe.delete()


def test_update_person_by_id(client):
    jane_doe = new_person(
        fname="Jane", mname="", lname="Doe", email="jd@missing.com", age=33
    )
    assert jane_doe is not None
    assert jane_doe.fname == "Jane"

    new_email = "jd@found.com"
    update_person_by_id(jane_doe.id, email=new_email)
    jane_doe = get_person(jane_doe.id)
    assert jane_doe.email == new_email

    jane_doe.delete()

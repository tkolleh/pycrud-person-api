import pytest
from person_api.services.person import get_persons
from person_api.models.person import Persons


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

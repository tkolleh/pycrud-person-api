import pytest
from person_api.services.person import Person, get_persons

class TestPerson:
    empty = Person('', '', '', '', None)
    full = Person('Nala', '', 'Lion', 'nl@cartoon.com', 22, '123abc')

    def test_dunder_str(self):
        assert str(self.empty) != ''
        assert 'Person{' in str(self.empty)
        assert ('mem_adr' in str(self.full) and self.full.id in str(self.full))

    def test_dunder_eq(self):
        assert self.empty != self.full
        self.full_dupe = self.full
        assert self.full_dupe == self.full

    def test_get_persons(self):
        persons = get_persons()
        assert len(persons) == 100



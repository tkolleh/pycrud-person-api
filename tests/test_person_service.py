import pytest
from person_api.person_service import Person

class TestPerson:
    empty = Person('', '', '', '', None)
    full = Person('Nala', '', 'Lion', 'nl@cartoon.com', 22, '123abc')
    
    def test_dunder_str(self):
        assert str(self.empty) != ''
        assert 'Person{' in str(self.empty)
        assert 'mem_adr' in str(self.full) and self.full.id in str(self.full)



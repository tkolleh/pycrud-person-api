"""
Service managing data for Person type
"""

from typing import str
from typing import int


class Person:
    def __init__(
        self, id: str, 
        fname: str, 
        mname: str, 
        lname: str, 
        email: str, 
        age: int
    ):
        self.id: str = id
        self.fname: str = fname
        self.mname: str = mname
        self.lname: str = lname
        self.email: str = email
        self.age: int = age

    def version(self) -> str:
        return "none"

    def __eq__(self, other) -> bool:
        pass

    def __str__(self) -> str:
        pass

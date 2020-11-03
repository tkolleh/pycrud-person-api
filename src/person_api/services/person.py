"""
Service managing data for Person type
"""
from person_api.db import fetch_persons
import json


class Person:
    """
    A class to represent a person.

    Attributes
    ----------
    fname: str
        first name of person
    mname: str
        middle name of person
    lname: str
        last name of person
    email: str
        email address of person
    age: int
        age of person
    """

    def __init__(
        self, fname: str, mname: str, lname: str, email: str, age: int, _id=None,
    ):
        self.id: str = _id if type(_id) == "str" else str(_id)
        self.fname: str = fname
        self.mname: str = mname
        self.lname: str = lname
        self.email: str = email
        self.age: int = age
        self.version: str = None

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __eq__(self, other) -> bool:
        return (
            self.id == other.id
            and self.fname == other.fname
            and self.mname == other.mname
            and self.lname == other.lname
            and self.email == other.email
            and self.age == other.age
            and self.version == other.version
        )

    def __str__(self):
        return (
            "{cname}{{ \nmem_adr='{mem_adr}', "
            "\n{id}, "
            "\n{version}, "
            "\n{fname}, "
            "\n{mname}, "
            "\n{lname}, "
            "\n{email}, "
            "\n{age}, "
            "\n}}".format(
                cname=self.__class__.__name__,
                mem_adr=id(self),
                id=self.id,
                version=self.version,
                fname=self.fname,
                mname=self.mname,
                lname=self.lname,
                email=self.email,
                age=self.age,
            )
        )


def get_persons():
    persons = (fetch_persons())[0]
    rtn = [Person(**p) for p in persons]
    return rtn

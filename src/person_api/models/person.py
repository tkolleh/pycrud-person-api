import json
from flask_mongoengine import MongoEngine

_DB = MongoEngine()


class Persons(_DB.Document):
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

    fname: str = _DB.StringField()
    mname: str = _DB.StringField()
    lname: str = _DB.StringField()
    email: str = _DB.StringField()
    age: int = _DB.IntField()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __eq__(self, other) -> bool:
        return (
            self.fname == other.fname
            and self.mname == other.mname
            and self.lname == other.lname
            and self.email == other.email
            and self.age == other.age
        )

    def __str__(self):
        return (
            "{cname}{{ \nmem_adr='{mem_adr}', "
            "\n{id}, "
            "\njson_str:'{obj_str}' "
            "\n}}".format(
                cname=self.__class__.__name__,
                mem_adr=id(self),
                id=self.id,
                obj_str=self.to_json(),
            )
        )

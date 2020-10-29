"""
Service managing data for Person type
"""


class Person:
    def __init__(
        self,
        fname: str,
        mname: str,
        lname: str,
        email: str,
        age: int,
        id: str = None,
    ):
        self.id: str = id
        self.fname: str = fname
        self.mname: str = mname
        self.lname: str = lname
        self.email: str = email
        self.age: int = age
        self.version: str = None

    def __eq__(self, other) -> bool:
        return (self.id == other.id and self.fname == other.fname
                and self.mname == other.mname and self.lname == other.lname
                and self.email == other.email and self.age == other.age
                and self.version == other.version)

    def __str__(self):
        return "{cname}{{ \nmem_adr='{mem_adr}', \n{id}, \n{version}, \n{fname}, \n{mname}, \n{lname}, \n{email}, \n{age}, \n}}".format(
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

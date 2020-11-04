"""
Database client module for interfacing with MongoDB.
"""
from flask_mongoengine import MongoEngine

from .models.persons import Persons, PersonRevisions


def init_db(app):
    """
    Configuration method to setup a global db instance
    """
    db = MongoEngine()
    db.init_app(app)
    return db


def fetch_persons(per_page=100, page=1, order_by: str = "lname"):
    paginated_docs = Persons.objects.order_by(order_by).paginate(
        page=page, per_page=per_page
    )
    return paginated_docs


def fetch_person(id: str):
    document = Persons.objects(id=id)
    return document


def save_person(p: Persons):
    p.save()


def save_person_revisions(pr: PersonRevisions):
    pr.save()


def set_person_fields(p, **kwargs):
    curr_person = fetch_person(p.id)[0]
    revision = 1 if curr_person.revision is None else curr_person.revision
    revised_person = PersonRevisions(
        age=curr_person.age,
        email=curr_person.email,
        fname=curr_person.fname,
        origin_id=str(curr_person.id),
        lname=curr_person.lname,
        mname=curr_person.mname,
        revision=revision,
    )
    save_person_revisions(revised_person)
    new_args = kwargs
    new_args["revision"] = revision + 1
    Persons.objects(id=p.id).update_one(**new_args)


def delete_person(p):
    p.delete()

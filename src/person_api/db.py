"""
Database client module for interfacing with MongoDB.
"""
from flask_mongoengine import MongoEngine

from .models.person import Persons


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


def set_person_fields(p, **kwargs):
    Persons.objects(id=p.id).update_one(**kwargs)


def delete_person(p):
    p.delete()

from mongoengine import *


class Edu(Document):
    name = StringField()
    search_name = StringField()
    district = StringField()
    city = IntField()
    fee = IntField()
    section = IntField()
    phone = StringField()
    rate = IntField()
    courses = ListField(StringField())

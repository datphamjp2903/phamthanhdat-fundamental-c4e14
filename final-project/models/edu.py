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
    photo1 = StringField()
    photo2 = StringField()
    photo3 = StringField()
    info = StringField()
    email = StringField()
    website = StringField()

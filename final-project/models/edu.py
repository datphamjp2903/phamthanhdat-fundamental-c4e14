from mongoengine import *


class Edu(Document):
    name = StringField()
    search_name = StringField()
    address = StringField()
    district = StringField()
    city = IntField()
    fee = IntField()
    section = IntField()
    phone = StringField()
    logo = StringField()
    photo1 = StringField()
    photo2 = StringField()
    photo3 = StringField()
    info = StringField()
    email = StringField()
    website = StringField()
    hot = BooleanField()

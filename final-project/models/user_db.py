from mongoengine import *



class Acc(Document):
    acc_id = StringField()
    acc_pass = StringField()
    role = BooleanField()
    rate = ListField(StringField())

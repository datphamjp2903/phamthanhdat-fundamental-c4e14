from mongoengine import Document, StringField, IntField, BooleanField

class excuse(Document):
    section = StringField()
    situation = StringField()
    content = StringField()
    rating = IntField()
    used = IntField()
    typical_mark = BooleanField()

#2 bai con lai t de o pilot-app

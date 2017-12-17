from mlab import mlab_connect
from models.service import Service

from random import choice, randint
from faker import Faker

service_faker = Faker()
mlab_connect()

Service.drop_collection() #delete documents

for _ in range(30):
    service = Service(name = service_faker.name(),
                  yob = randint(1987, 1998),
                  gender = randint(0, 1),
                  height = randint(150, 180),
                  phone = "09696969",
                  occupied = choice([True, False])
                  )
    service.save()

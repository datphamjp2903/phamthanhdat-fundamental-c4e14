from mlab import mlab_connect
from models.edu import Edu

from random import *
from convert import convert
mlab_connect()

for _ in range(30):
    edu = Edu(name = 'Trung Tâm {}'.format(_ + 1),
              search_name = 'trung tam {}'.format(_ + 1),
              address = '',
              district = choice(['Quận 1', 'Quận 2', 'Quận 3','Quận A', 'Quận B', 'Quận C']),
              city = randint(1, 3), #1: HN, 2:HCM, 3:DN
              fee = choice([1000000, 20000000, 2000000, 10000000, 15000000, 5000000]),
              section = randint(1, 4), #1:anh , 2:nhat, 3:phap, 4:lap trinh
              phone = '01679773969',
              logo = '',
              photo1 = '',
              photo2 = '',
              photo3 = '',
              info = '',
              email = '',
              website = '')
    edu.save()

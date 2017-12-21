from mlab import mlab_connect
from models.service import Service

mlab_connect()

female = Service.objects(gender = 0, height__gte = 160, occupied = False)
for girl in female:
    print(girl)

# female.first().delete()
# female.first().reload()
if female is None:
    print("Not found")
else:
    for girl in female:
        girl.update(set__occupied = True)
        girl.reload()
        print(girl, girl.occupied)

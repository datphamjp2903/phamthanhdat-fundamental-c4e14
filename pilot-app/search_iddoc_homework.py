from mlab import mlab_connect
from models.service import Service

mlab_connect()

services = Service.objects()
id_to_find = services.get(id = '5a3629a60fe8e82350828328')
print(id_to_find.name)

for id_to_find in services:
    if str(id_to_find.id) == '5a3629a60fe8e82350828328':
        print(id_to_find.name)

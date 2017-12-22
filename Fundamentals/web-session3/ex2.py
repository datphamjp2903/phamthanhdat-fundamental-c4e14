from ex1 import mlab_connect
from models.river import River

mlab_connect()

rivers = River.objects(continent = 'Africa')

if len(rivers) == 0:
    print("Not found")
else:
    for river in rivers:
        print(river)

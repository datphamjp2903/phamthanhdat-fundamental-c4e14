from ex1 import mlab_connect
from models.river import River

mlab_connect()

rivers = River.objects(continent = 'S. America', length__lt = 1000)

if len(rivers) == 0:
    print("Not found")
else:
    for river in rivers:
        print(river, river.length)

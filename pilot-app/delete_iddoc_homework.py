from mlab import mlab_connect
from models.service import Service

mlab_connect()

services = Service.objects()

services(name = 'Sara Bell').delete()
# x.objects().delete()

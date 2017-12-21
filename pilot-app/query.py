from mlab import mlab_connect
from models.service import Service

mlab_connect()

# all_services = Service.objects()
#
# for service in all_services:
#     print(service.name)

# id_to_find = "5a3629a60fe8e82350828327"
# # tammy = Service.objects(id = id_to_find).first() #filter, get first key, use when find by id, regular search
# tammy = Service.objects().with_id(id_to_find) #search by id only
#
# if tammy is None:
#     print("Not found")
# else:
#     print(tammy.name)
#     tammy.delete()

id_to_find = "5a3629a70fe8e8235082832b"
mitchell = Service.objects().with_id(id_to_find)

if mitchell is None:
    print("Not found")
else:
    print(mitchell.name)
    mitchell.update(set__occupied = False) #inc__ (increase)
    mitchell.reload() #sync value

# mongodb://<dbuser>:<dbpassword>@ds249787.mlab.com:49787/project_c4e

import mongoengine

host = "ds249787.mlab.com"
port = 49787
db_name = "project_c4e"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())

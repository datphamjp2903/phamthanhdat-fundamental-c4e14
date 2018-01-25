from mlab import mlab_connect
from models.accounts import Acc

from random import *
from convert import convert
mlab_connect()

new_acc = Acc(acc_id = "client",
              acc_pass = "client",
              role = False,
              rate = [])
new_acc.save()

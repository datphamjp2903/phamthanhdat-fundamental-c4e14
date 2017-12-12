from bt11 import *

a = is_inside([100, 120], [140, 60, 100, 200])
if not a:
    print("Your function is correct.")
else:
    print("Bug.")

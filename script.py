import os
from numpy import log

a = float(os.environ.get("A"))
b = float(os.environ.get("B"))

print ("log a * b")
print(log(a * b))
print ("log a + log b")
print(log(a) + log(b))
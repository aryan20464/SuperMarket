import re

x, y, z = "hello", 1, "213"

if type(x) is str:
    print "string"
else:
    print "not string"


xc = re.findall("\S[0-9]+\S", z)[0]
print int(xc)
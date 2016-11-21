import numpy

names = list()
for x in range(0, 5):
    names.insert(x, str(raw_input("\n Enter a name : ")))

matrix = [['' for x in range(3)]for x in range(5)]

for row in range(0, 5):
    matrix[row][0] = "*"
    matrix[row][1] = names[row]
    matrix[row][2] = "*"

for x in range(0, 5):
    print "%s \t %-10s \t %s" %(matrix[x][0], matrix[x][1], matrix[x][2])
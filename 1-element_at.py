import random
import math
randlist = ["string", 1.24, 28]

oneToTen = list(range(10))

randlist = randlist + oneToTen

print(randlist[0])

print("list length :", len(randlist))

first3 = randlist[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0] * 3)

print("string" in first3)

print("index of string :", first3.index("string"))

print("how many strings : ", first3.count("string"))

for i in first3:
    print("{} : {}".format(first3.index(i), i))

first3.append("Another")

for i in first3:
    print("{} : {}".format(first3.index(i), i))

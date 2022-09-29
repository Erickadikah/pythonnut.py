# from functools import reduce
# f = lambda a,b: a if (a > b) else b
# reduce(f, [47,11,42,102,10])

#error handling.

try:
    myFile = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("that file was not found")

    print(ex.args)

else:
    print("file :", myFile.read())
    myFile.close()

finally:
    print("finished working with file")
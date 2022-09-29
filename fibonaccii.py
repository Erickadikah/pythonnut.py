def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result



numfibValues = int(input("how many fibonacci values shoul be found : "))
i = 1
while 1 < numfibValues:

    fibValue = fib(i)

    print(fibValue)

    i += 1

print("all done")
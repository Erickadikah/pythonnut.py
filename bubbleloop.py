import random
import math

#1. An outer loop decreases in size each time
#2. The goal is to have the largest numbre ta the end of the list
# when the outer looop cempletes 1 cycle
#3. the inner loop starts comparing indexes at the beginign of the loop
#4. check is lists[Idex] > list[Index + 1]
#5. if so swap the index values
#6. when the inner loop completes the largest number is at
#the end of the list
#7. decrement the outer loop by 1


import random
import math

numlist = []

for i in range(5):
    numlist.append(random.randrange(1, 10))

i = len(numlist) - 1

while i > 1:

    j = 0

    while j < i:

        if numlist[j] > numlist[j + 1]:

            temp = numlist[j]
            numlist[j] = numlist[j + 1]
            numlist[j + 1] = temp
        else:
            print()

        j += 1

    i -= 1

for k in numlist:
    print(k, end=", ")
print()








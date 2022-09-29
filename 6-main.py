bill = 0
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
if height >= 120:  # comparison operator
    print("you can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("childs tickets are  $ 5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are  $7.")
    else:
        bill = 12
        print("adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
       bill = bill + 3 # bill +=3

    print(f" your final bill is ${bill}")


else:
    print("sorry, you have to grow taller before you can ride.")

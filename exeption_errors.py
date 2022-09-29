# try:
#     a_list = [1,2,3]
#
#     print(a_list[3])
#
# except IndexError:
#     print("sorry that index doest")
# #eccept("indexerror, nameerror")
# except:
#     print("An unknown error occured")
# #also posible for custom error

class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogname = input("whats is your dog name : ")

    if any(char.isdigit() for char in dogname ):
        raise DogNameError
except DogNameError:
    print("your dogs name can't contain a number")

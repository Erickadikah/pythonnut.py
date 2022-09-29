# def test_var_args(f_arg, *argv):
#     print("first normal arg:",).f_arg
#     for arg in argv:
#         print("another arg through *argv :",).arg
#
# test_var_args('yasoob','python','eggs','test')
# def person (name, **data):
#      print(name)
#      for i,j in data.items():
#          print(i,j)
#
#
#
#
# person('erick adikah', age=22, city='Nairobi', mob=97901001)

def my_func(*args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", key=123, abc=123)


# def calcfunvalue(*args):
#     print(args)
#     totalvalue = sum(args)
#     return(totalvalue)
# print()
#
#
#
# calcfunvalue(10,20,30,46)
# print()


def news(**kwargs):
    mystr = kwargs['player'] + "scored" + kwargs['runs'] + "runs"
    return(mystr)
    if 'place' in kwargs:
        mystr = mystr+" in "+kwargs['place']


news(player="erick", runs="2000", place="Nairobi")
# class Person:
#
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#      print(self.lastname, self.firstname)
#
#
# x = Person("Erick", "Adikah")
# x.printname()


#
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
#
#         def welcome(self):
#             print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#
#
#
# x = Student("mike", "olsen", 2019)
# x.printname()
# print()
# class A:
#     def feature1(self):
#         print("feature 1 is working")
#
#     def feature2(self):
#         print("feature 2 is working.")
#
#
# class B(A):
#     def feature3(self):
#         print("feature 1 is working")
#
#     def feature4(self):
#         print("feature 2 is working")
#
#
# a1 = A()
#
#
# a1.feature1()
# a1.feature2()
#
# b1 = B()
#
# b1.feature4()


# class Base():
#     """ My base class """
#
#     __nb_instances = 0
#
#     def __init__(self):
#         Base.__nb_instances += 1
#         self.id = Base.__nb_instances
#
# class User(Base):
#     """ My User class """
#
#     def __init__(self):
#         super().__init__()
#         self.id += 99
#
# u = User()
# print(u.id)

# class Base():
#     """ My base class """
#
#     __nb_instances = 0
#
#     def __init__(self):
#         Base.__nb_instances += 1
#         self.id = Base.__nb_instances
#
# class User(Base):
#     """ My User class """
#     pass
#
# b = Base()
# u = User()
# print(u.id)


class Animal:
    def __init__(self, birthtype="Unknown", appearance="Unknown", blooded="Unknown"):
        self.birthtype = birthtype
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthtype(self):
        return self.__birthtype

    @birthtype.setter
    def birthtype(self, birthtype):
        self.__birthtype = birthtype

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} it is {} ".format(type(self).__name__,self.birthtype, self.appearance, self.blooded)


class Mammal(Animal):
    def __init__(self, birthtype="born alive", appearance="hair or fur", blooded="warm blooded", nurseyoung=True):
        Animal.__init__(self, birthtype, appearance, blooded)

        self.__nurseYoung = nurseyoung

        @property
        def nurseyoung(self):
            return self.__nurseYoung

        @nurseyoung.setter
        def nurseyoung(self, nurseyoung):
            self.__nurseyoung = nurseyoung

        def __str__(self):
            return super().__str__() + "it is {} they nurse their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthtype="born in an egg or born alive", appearance="dry scales", blooded="cold blooded"):
        Animal.__init__(self, birthtype, appearance, blooded)



    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i
        return sum
def getbirthtype(theObject):
    print("the {} is {}".format(type(theObject).__name__, theObject.birthtype))

def main():
    animal1 = Animal("born alive")

    print(animal1.birthtype)
    print(animal1.blooded)
    print(animal1.appearance)

    print(animal1)
    print()

    mammal1 = Mammal()

    print(mammal1.birthtype)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1)
    print()

    reptile1 = Reptile()

    print(reptile1.birthtype)
    print(reptile1.appearance)
    print(reptile1.blooded)
    print(reptile1)

    print("sum : {}".format(reptile1.sumAll(1, 2, 3, 4, 5)))

    getbirthtype(mammal1)
    getbirthtype(reptile1)





main()

# class Polygon:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def display_info(self):
#         print("a polygon has five sides")
#
#     def get_perimeter(self):
#         perimeter = sum(self.sides)
#         return perimeter
#
#
# class Triangle(Polygon):
#     def display_info(self):
#         print("a triangle is a polygon with three egdes.")
#
#
#
# class Quadriletral(Polygon):
#     def display_info(self):
#         print("a quadrilateral is a polygon with 4 edges")
#
#
#
# t1 = Triangle([5, 6, 7])
# perimeter = t1.get_perimeter()
# print("the perimeter", perimeter)
# t1.display_info()
#
# t2 = Quadriletral([10, 12, 17])
# perimeter = t2.get_perimeter()
# print("a quadrilateral is", perimeter)
# t2.display_info()


#Example 2


# class Animal:
#     def eat(self):
#         print("yum yum")


# class Dog(Animal):
#     def bark(self):
#         print("i can bark")
#
#
# class Cat(Animal):
#     def get_grumpy(self):
#         print("meow meow")
#
# class Lion(Animal):
#     def get_angry(self):
#         print("Roar")
#
#
#
# dog1 = Dog()
# dog1.bark()
# dog1.eat()
#
# cat1 = Cat()
# cat1.get_grumpy()

# lion1 = Lion()
# lion1.get_angry()
# lion1.eat()

#

class Person:
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

    def display(self):
        print(self.name, self.Id)


Emp = Person("erick ", 38620361)
Emp.display()

class Cook(Person):
    pass


Emp = Cook("mike", 456778)
Emp.display()


class Student(Person):
    pass


Emp = Person("mike", 6787689)
Emp.display()
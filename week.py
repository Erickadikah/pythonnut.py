class Person:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def walk(self):
        print("{}  walks".format(self.name))

    def eats(self):
        print("{} eats ugali and sukuma".format(self.name))

    def run(self):
        print("{} runs fast".format(self.name))

# def main():
#
#         erick = Person("erick",66, 26)
#
#         erick.walk()
#
#         erick.eats()
#
#         erick.run()
#
#
# main()

class Rectangle:
    def __init__(self, lenth="0", width="0"):
        self.lenth = lenth
        self.width = width

    @property
    def lenth(self):
        print("Retrieving the height")

        return self.__lenth
    @lenth.setter
    def lenth(self, value):

        if value.isdigit():
            self.__lenth = value
        else:
            print("please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the width")

        return self.__width

    @lenth.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("please only enter numbers for width")
    def getArea(self):
        return int(self.lenth) * int(self.__width)

def main():
    aRectangle = Rectangle()

    lenth = input("Enter lenth :")
    width = input("Enter width :")

    aRectangle.lenth = lenth
    aRectangle.width = width

    print("lenth :", aRectangle.lenth)
    print("width :", aRectangle.width)

    print("the area is :", aRectangle.getArea())
main()
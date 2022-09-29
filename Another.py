class Triangle:
    def __init__(self, lenth=0, width=0, height=0):
        self.lenth = lenth
        self.width = width
        self.height = height
@property
def lenth(self):
    print("Retreaving the lenth")

    return self.__lenth
@lenth.setter
def lenth(self, value):
        if value.isdigit():
            self.__lenth = value
        else:
            print("please only enter numbers for height")


@property
def width(self):
    print("Retreaving the width")

    return self.__lenth


@width.setter
def width(self, value):
    if value.isdigit():
        self.__width = value
    else:
        print("please only enter numbers for width")

@property
def height(self):
    print("Retreaving the height")

    return self.__height

@height.setter
def width(self, value):
    if value.isdigit():
        self.__width = value
    else:
        print("please only enter numbers for width")
def getArea(self):
    return int(self.lenth) * int(self.width) * int(self.height)

def main():
    aTriangle = Triangle()

    lenth = input("Enter Lenth : ")
    width = input("Enter Width : ")
    height = input("Enter Height : ")

    aTriangle.lenth = lenth
    aTriangle.width = width
    aTriangle.height = height

    print("Lenth :", aTriangle.height)
    print("Width :", aTriangle.width)
    print("Height:", aTriangle.height)

    print("The Area is :", getArea(self))


main()




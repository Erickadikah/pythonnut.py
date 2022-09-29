# from calculator import square
#
# def main():
#     test_spuare()
#
# def test_spuare():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")
#
#
# if __name__ == "__main__":
#     main()
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(0) == 0
    assert square(-2) == 4

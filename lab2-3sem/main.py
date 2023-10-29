from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
def main():
    r = Rectangle(1, 2, "красного")
    c = Circle(1, "зеленого")
    s = Square(2, "синего")
    print(r)
    print(c)
    print(s)
if __name__ == "__main__":
    main()

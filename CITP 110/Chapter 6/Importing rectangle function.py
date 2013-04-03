import rectangle

def main():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print("The area is", rectangle.area(width, length))
    print("The perimeter is", rectangle.perimeter(width, length))
    
main()
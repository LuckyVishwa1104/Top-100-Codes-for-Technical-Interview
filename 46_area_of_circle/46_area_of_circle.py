# Python program to find area of circle
import math

# method 1 - using formula
try:
    n=eval(input("Enter the radius :"))
    area=3.14*(n)**2
    print("area is =",area)
except:
    print("Enter a valid value...")

# method 2 - id diameter is given
try:
    n=eval(input("Enter the diameter :"))
    area=3.14*(n/2)**2
    print("area is =",area)
except:
    print("Enter a valid input...")

# method. 3 - using module based approach

def circle_area(radius):
    return lambda radius : (math.pi * (radius ** 2))

try:
    while (True):
        num = int(input("Enter a Integer value: "))

        result = circle_area(abs(num))
        print(f"Area of Circle with radius {num} : {result}")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice.lower() == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")


# Python program to find area of circle

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

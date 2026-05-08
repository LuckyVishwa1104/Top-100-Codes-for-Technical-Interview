# python program to find greatest among three number

# method 1 - traditional method

try:
    a=eval(input("Enter first number :"))
    b=eval(input("Enter second number :"))
    c=eval(input("Enter third number :"))
    if a>b:
        if a>c:
            print(f'{a} is greatest')
        else:
            print(f"{c} is greatest")
    else:
        if b>c:
            print(f"{b} is greatest")
        else:
            print(f"{c} is greatest")
except:
    print("Enter valid numeric value!")

# method 2 - using ternary operator

try:
    a=eval(input("Enter first number :"))
    b=eval(input("Enter second number :"))
    c=eval(input("Enter third number :"))
    print(f'{a} is greatest' if a>b and a>c else f'{b} is greatest' if b>a and b>c else f'{c} is greatest')
except:
    print("Enter Valid numeric value!")

# method 3 - function based approach

def greatest_among_three(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c
    
try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = int(input("Enter third number : "))

    if (a == b == c):
        print("Given numbers are equal")
    else:
        result = greatest_among_three(a, b, c)
        print(f"{result} is greates among {a}, {b}, {c}")

except ValueError as e:
    print(f"Invalid input : {e}")

except Exception as e:
    print(f"Excetion caught : {e}")


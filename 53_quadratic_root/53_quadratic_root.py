# Python program to find quadratic root

# method 1 - using brut force
# quadratic root - i**2 = -1 | i=(-1)**(1/2)

a=int(input("Enter the coefficient of x^2 :"))
b=int(input("Enter the coefficient of x :"))
c=int(input("Enter the constant term :"))

D=(b**2 -4*a*c)**0.5
if type(D)==complex:
    print("There exist two real solutions.")
    x1=(-b+D)/(2*a)
    x2=(-b-D)/(2*a)
    print("first solution :",x1)
    print("second solution :",x2)

elif D==0:
    print("There exist unique solution.")
    x=-b/(2*a)
    print("root is :",x)

else:
    print("There exits imaginary solution.")
    x1=(-b+D)/2*a
    x2=(-b-D)/2*a
    print("first solution :",x1)
    print("second solution :",x2)

# method 2 - using module based approach

def roots(a, b, c):
    D = ((b ** 2) - 4 * a * c) ** 0.5

    if (0 == D):
        x1 = b / 2*a
        return (x1)
    
    else:
        x1 = (-b + D) / (2 * a)
        x2 = (-b - D) / (2 * a)
        return (x1, x2)

try:
    while (True):
        
        a=int(input("Enter the coefficient of x^2 :"))
        b=int(input("Enter the coefficient of x :"))
        c=int(input("Enter the constant term :"))

        result = roots(a, b, c)
        print(f"{result}")

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


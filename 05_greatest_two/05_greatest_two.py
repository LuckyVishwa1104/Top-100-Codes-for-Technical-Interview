# # python program to find greatestbetween two numbers

# method 1 - tradtional method
try:
    n=eval(input("Enter first number :"))
    m=eval(input("Enter second  number :"))
    if n>m:
        print(f'{n} is greater.')
    elif n<m:
        print(f'{m} is greater')
    else:
        print("Number are equal.")
except:
    print("Enter valid numeric value!")

# method 2 - using ternary operator
try:
    n=eval(input("Enter first number :"))
    m=eval(input("Enter second  number :"))
    print("Numbers are equal" if n==m else f"{n} is greater." if n>m else f"{m} is greater")
except:
    print("Enter a valid numeric value!")


def greatest_among_two(a, b):
    if (a < b):
        return b
    else :
        return a
    
try:
    a = int(input('Enter integer value : '))
    b = int(input("Enter integer value : "))

    if (a == b):
        print("Number are equal")
    else:
        result = greatest_among_two(a, b)
        print(f"Greatest number is {result}")

except ValueError as e:
    print(f"Invalid Input : {e}")
    
except Exception as e:
    print(f"Exception caught : {e}")
    


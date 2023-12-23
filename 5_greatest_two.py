# python program to find greatestbetween two numbers

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

    
# python program to check prime number or not

# method 1 - using third variable
try:
    n=eval(input("Enter the number :"))
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    if flag==True:
        print(f'{n} is a prime number.')
    else:
        print(f'{n} is not a prime number.')
except:
    print("Enter a valid numeric value")

# method 2 - using for-else combination
try:
    n=eval(input("Enter the number :"))
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f'{n} is a Prime number.')
    pass
except:
    print("Enter a valid numeric value.")

# method 3 - uning iteration upto n/2 only
try:
    n=eval(input("Enter the number :"))
    for i in range(2,(n//2)+1):
        if n%i==0:
            print(f'{n} is not a Prime number.')
            break
    else:
        print(f'{n} is a Prime number.')
    pass
except:
    print("Enter valid numneric value.")

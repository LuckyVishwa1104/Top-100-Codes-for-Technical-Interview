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

# method 4 - using the number of divisor
# prime number have only two divisors
n=int(input("Enter the number :"))
cnt=0
for i in range(1,n+1):
    if n%i == 0:
        cnt+=1
if cnt==2:
    print(n,"is a PRIME number.")
else:
    print(n,"is not a prime number.")

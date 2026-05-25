# Strong number - a number is a strong number if the sum of factorial of each digit in number is equal to number itself

# method 1 - using iteration
try:
    n=int(input("Enter the number :"))
    m=n
    sum=0
    while sum<m:
        n1=n%10
        n=n//10
        fac=1
        for i in range(1,n1+1):
            fac=fac*i
        sum=sum+fac     
    if sum==m:
        print(f"{m} is a Strong Number.")
    else:
        print(f"{m} is not a Strong Number.")
except:
    print("Enter a valid number.")

# method 2 - using recurssion
try:
    n2=int(input("Enter a number :"))
    sum=0
    def strong_number(n2):
        if n2==0:
            return print(end="")
        n1=n2%10
        def fac(n1):
            if n1==0:
                return 1
            facc=n1
            return facc*fac(n1-1)
        global sum
        sum=sum+fac(n1)
        strong_number(n2//10)
    strong_number(n2)
    if sum==n2:
        print(f"{n2} is a Strong number")
    else:
        print(f"{n2} is not a Strong number")
except:
    print("Enter a valid integer value")

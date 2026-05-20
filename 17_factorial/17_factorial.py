# pyhton program to find the factorial of a nunmber

# mehtod 1 - by using simple iteration
try:
    n=int(input("Enter a number :"))
    fac=1
    if n<0:
        print("Enter a value greater than or equal to ZERO")
    else:
        for i in range(1,n+1):
            fac=fac*i
        print(fac)
except:
    print("Enter a valid integer value!")

# method 2 - using recurssion 
try:
    n=int(input("Enter a number :"))
    if n<0:
        print("Enter a value greater than or equal to ZERO")
    else:
        def fac(a):
            if a==0:
                return 1
            return a*fac(a-1)
        print(fac(n))
except:
    print("Enter a valid integer value.")

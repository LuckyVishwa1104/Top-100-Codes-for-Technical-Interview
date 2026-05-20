# python program to find factors of a number
# factor of a number are the nunmbers that can divide the given number perfectly

# method 1 - using simple iteration 
try:
    n=int(input("Enter the number :"))
    if n<0:
        print("Enter number greater than or equal to Zero")
    else:
        for i in range(1,(n//2)+1):
            if n%i==0:
                print(i,end=" ")
        print(n)
except:
    print("Enter a valid integer value!")

# method 2 - using recurssion
try:
    n=int(input("Enter number :"))
    def fac(a):
        if a>n//2:
            return print(n)
        if n%a==0:
            print(a,end=' ')
        fac(a+1)
    fac(1)
except:
    print("Enter a valid integer value!")

# python progfram to display Armstrong numbers in a particular range or sequence

# method 1 - by using simple iteration 
try:
    m=int(input("Enter the number :"))
    for i in range(1,m+1):
        n=str(i)
        sum=0
        l=len(n)
        for j in n:
            sum=sum+(int(j)**l)
        if n==str(sum):
            print(n)
except:
    print("Enter a valid integer number.")

# method 2 - within particular range
a=int(input("Enter starting number :"))
b=int(input("Enter ending number :"))
try:
    for i in range(a,b+1):
        n=str(i)
        sum=0
        l=len(n)
        for j in n:
            sum=sum+(int(j)**l)
        if n==str(sum):
            print(n)
except:
    print("Enter a valid integer number.")
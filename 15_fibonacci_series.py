# python program to display FIBONACCI series upto nth number
# fibonacci series is a sequence of number for which every third number is the sum of previous two numbers

# method 1 - using simple iteratrion
try:
    n=int(input())
    n1=0
    print(n1)
    n2=1
    while n2<=n:
        print(n2)
        n3=n1+n2
        n1=n2
        n2=n3
except:
    print("Enter a valid number")

# method 2 - using recurssion
try:
    n=int(input())
    n1=0
    print(n1,end=" ")
    n2=1
    print(n2,end=" ")
    def fibb(n1,n2):
        n3=n1+n2
        n1=n2
        n2=n3
        if n2>n:
            return ""
        return str(n2)+" "+str(fibb(n1,n2))
    print(fibb(n1,n2))
except:
    print("Enter a valid integer value number.")
    


# Python program to find power of a number using recursion

# method 1 - using recursion
try:
    n=int(input("Enter the number :"))
    m=int(input("Enter the power number :"))
    pro=1
    def powr(a):
        if a>m:
            return
        global pro
        pro=pro*n
        powr(a+1)
    powr(1)
    print(pro)
except:
    print("Something went wrong!!!")

# method 2 - 
try:
    n=int(input("Enter the number :"))
    m=int(input("Enter the power number :"))
    def fac(n,m):
        if m==0:
            return 1
        return n*fac(n,m-1)
    print(fac(n,m))
except:
    print("Something went wrong!!!")


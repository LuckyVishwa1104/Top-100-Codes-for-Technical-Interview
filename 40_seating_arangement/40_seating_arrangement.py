# Python program to find number of ways in which n person can seat on r seats

# method 1 - using permutation formula by recursion
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
try:
    n=int(input("Enter number of persons :"))
    m=int(input("Enter number of seats :"))
    def fac(a):
        if a==0:
            return 1
        facc=a
        return facc*fac(a-1)
    aa=fac(n)
    bb=fac(n-m)
    ways=aa//bb
    print(ways)
except:
    print("Enter valid integer values.")

# method 2 - using iteration
try:
    n=int(input("Enter number of persons :"))
    m=int(input("Enter number of seats :"))
    def fac(a):
        fac=1
        for i in range(1,a+1):
            fac=fac*i
        return fac
    ways=fac(n)//fac(n-m)
    print(ways)
except:
    print("Enter valid values")


# python program to find prime factorials of a numbers
# factor - factores of a number are the numbers which completely divides the number

# method 1 - using iterations
try:
    n=int(input("Enter the number :"))
    for i in range(2,n+1):
        if n%i==0:
            for j in range(2,(i//2)+1):
                if i%j==0:
                    break
            else:
                print(i)
except:
    print("Enter a valid integer values!")

# following recursion will iterate only upto 1000 times due to default value, hence it will provide result for upto 1000 number as input
# to increse the limit following code is used
import sys
sys.setrecursionlimit(2000)  # it  will set the recursion limit to 2000 iterations

# method 2 - using recurssion
l=int(input('Enter Number :'))
if l%2==0:
    print(2)
def p_fac(n):
    if n>l:
        return print(end="")
    if l%n==0:    
        def prm(p,k1=n): 
            if k1%p==0:
                return print(end="")
            if p==k1-1:
                return print(k1)
            prm(p+1)
        prm(2)
    p_fac(n+1)
p_fac(2)



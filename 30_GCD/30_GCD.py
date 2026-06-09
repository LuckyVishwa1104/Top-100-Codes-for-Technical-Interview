# Pyhton program to find GCD of a given number
# GCD - greatest common divisor is the largest common number that completely divides the given two numbers

# method 1 - using iteration
a,b=map(int,input("Enter two space separate numbers :").split(" "))
for i in range(min(a,b)):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

# method 2 - using recursion
a,b=map(int,input("Enter two space separate numbers :").split(" "))
def fun1(i):
    if i>min(a,b):
        return print(end="")
    if a%i==0 and b%i==0:
        global gcd
        gcd=i
    fun1(i+1)
fun1(1)
print(gcd,"is the GCD")

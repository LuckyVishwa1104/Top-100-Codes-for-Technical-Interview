# PYHTON PROGRAM to find lowest common multiple of two numbers
# LCM - lcm is the lowest number of common multiples of the number

# method 1 - using iterations (this method is feasible for smaller number, not suitable for larger number)
a,b=map(int,input("Enter the two space separated numbers :").split(" "))
aa=False
for i in range(1,11):
    for j in range(1,11):
        if a*i == b*j:
            print(a*i,"is the LCM")
            aa=True
            break
    if aa:
        break

# using recursion
n,m=map(int,input().split())
lcm=0
t=False
def func1(a):
    if a>max(n,m):
        return
    def func2(b):
        if b>max(n,m):
            return
        if n*a == m*b:
            global lcm,t
            lcm=n*a
            t=True
            return
        func2(b+1)
    func2(1)
    if t:
        return
    func1(a+1)
func1(1)
print(lcm)

# method 2 - using formula LCM=(num1*num2)/HCF
a,b=map(int,input("Enter the two space separated numbers :").split(" "))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
lcm=(a*b)//hcf
print(f"{lcm} is the LCM")
# using recursion
def hcf_fun(i):
    if i>min(a,b):
        return print(end="")
    if a%i==0 and b%i==0:
        global hcf
        hcf=i
    hcf_fun(i+1)
    pass
hcf_fun(1)
lcm=(a*b)//hcf
print(lcm,"is LCM")


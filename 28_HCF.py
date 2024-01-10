# Python program to fing highest common factor of two numbers
# HCF - hcf is a number highest number that conbinely divides both the numbers

# method 1 - using Iteration
a,b=map(int,input("Enter the two space separated numbers :").split(" "))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
print(f"{hcf} is the HCF")

# method 2 - using recursion
a,b = map(int,input("Enter two space separated number :").split())
def hcf_fun(i):
    if i>min(a,b):
        return print(end="")
    if a%i==0 and b%i==0:
        global hcf
        hcf=i
    hcf_fun(i+1)
hcf_fun(1)
print(hcf,"is HCF")

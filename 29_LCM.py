# PYHTON PROGRAM to find lowest common multiple of two numbers
# LCM - lcm is the lowest number of common multiples of the number

# method 1 - using iterations (this method is feasible for smaller number, not suitable for larger number)
a,b=map(int,input("Enter the two space separated numbers :").split(" "))
# for i in range(1,11):
#     for j in range(1,11):
#         if a*i == b*j:
#             print(a*i,"is the LCM")
#             break

# using recursion
def fun(i):
    if i>10:
        return print(end="")
    def fun2(j):
        if j>10:
            return print(end="")
        if a*i == b*j:
            return print(a*i)
        fun2(j+1)
    fun2(i)
    fun(i+1)
fun(1)

# method 2 - using formula LCM=(num1*num2)/HCF
# a,b=map(int,input("Enter the two space separated numbers :").split(" "))
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         hcf=i
# lcm=(a*b)//hcf
# print(f"{lcm} is the LCM")
# using recursion
# def hcf_fun(i):
#     if i>min(a,b):
#         return print(end="")
#     if a%i==0 and b%i==0:
#         global hcf
#         hcf=i
#     hcf_fun(i+1)
#     pass
# hcf_fun(1)
# lcm=(a*b)//hcf
# print(lcm,"is LCM")


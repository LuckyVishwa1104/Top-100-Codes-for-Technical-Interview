# Python program to check whether the pair of given number is a friendly pair or not
# Friendly pair - two two number should be a perfect number then it si friendly pair

# method 1 - using iteration
# 1st - range(1,n+1)
# 2nd - range(1,n//2+1)  --- more fesible (complexity reduces by half times)
# 3rd - range(1,sqrt(n))  --- most feasible (complexity reduces by square root times)

n,m=map(int,input("Enter the space separated number :").split(" "))
result1 = result2 = False
for i in n,m:
    sum=0
    for j in range(1,i//2+1):
        if i%j==0:
            sum=sum+j
    if i==sum:
        if i==n:
            result1=True
        elif i==m:
            result2=True
if result1 and result2:
    print("It is a Friendly pair")
else:
    print("It is not a friendly pair")

# method 2 - using functions and recurssion
a,b=map(int,input().split())
def fun(m):
    global sum
    sum=0
    def rec(n):
        if n==m//2+1:
            return sum
        if m%n==0:
            sum=sum+n
        rec(n+1)
    rec(1)
if fun(a)==a and fun(b)==b:
    print("It is a Friendly Pair")
else:
    print("It is not a Friendly Pair")

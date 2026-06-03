# Python program to check whether the pair of given number is a friendly pair or not
# Friendly pair - two two number should be a perfect number then it si friendly pair

# method 1 - using iteration
# 1st - range(1,n+1)
# 2nd - range(1,n//2+1)  --- more fesible (complexity reduces by half times)
# 3rd - range(1,sqrt(n))  --- most feasible (complexity reduces by square root times)

from math import sqrt

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

# method. 3 - using module based approach

def proper_factor(num):
    factor_list = [ i for i in range(1, num//2+1) if num%i==0]
    return factor_list

def is_friendly(num1, num2):
    if num1 == num2:
        return False
    sum1 = sum(proper_factor(num1))
    sum2 = sum(proper_factor(num2))
    return (num1==sum2 and num2==sum1)

try:
    while(True):
        num1 = int(input("Enter positive integer value : "))
        num2 = int(input("Enter positive integer value : "))
        limit  = 1000
        if (num1 <= 0 or num2 <= 0):
            print("Enter positiveinteger value")
        elif (num1 > limit or num2 > limit):
            print("Input too large")
        else:
            result = is_friendly(num1, num2)
            if(result):
                print(F"{num1}, {num2} are Friendly Pair")
            else:
                print(F"{num1}, {num2} are not Friendly Pair")
        choice = input("Do you want to continue the program (y/n) : ")
        if(choice == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print("Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")



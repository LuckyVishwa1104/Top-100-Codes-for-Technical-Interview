# Python program to check whether a number is a abundant number or not]
# Abundant number - a number is abundant if the number is less than sum of its factors except the number itself.

# method 1 - using iteration
n=int(input("Enter the number :"))
sum=0
for i in range(1,n//2+1):
    if n%i == 0:
        sum=sum+i
if n<sum:
    print("It is an Abundant unmber")
else:
    print("It is not an Abundant number")

# method 2 - using recursion
n=int(input("Enter the number :"))
sum=0
def abundant_number(i):
    if i>n//2+1:
        return print(end="")
    global sum
    if n%i == 0:
        sum = sum+i
    abundant_number(i+1)
abundant_number(1)
if n<sum:
    print("It is a Abundant number.")
else:
    print("It is not a Abundant number.")



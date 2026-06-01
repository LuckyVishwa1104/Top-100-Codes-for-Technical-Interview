# Python program to check whether a number is a abundant number or not
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

# method 3 - using module based approach

def is_abundant(num):
    summ = 0
    for i in range(1, num):
        if(num % i == 0):
            summ = summ + i
    return (num < summ)

try:
    while(True):

        num = int(input("Enter positive integer value : "))
        limit  = 1000
        if (num <= 0):
            print("Enter positiveinteger value")
        elif (num > limit):
            print("Input too large")
        else:
            result = is_abundant(num)
            if(result):
                print(f"{num} is Abundant number")
            else:
                print(f"{num} is not a Abundant number")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print("Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print("Exception caught : {e}")


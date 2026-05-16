# python program to check wheteher a number is a armstrong nuber or not a armstrong number
# an ARMSTRONG number is a number for which the sum of each digit of number raised to the power of total digit present in number is equal to number itself

# method 1 - by using simple iteration
try:
    n=input("Enter number :")
    sum=0
    l=len(n)
    for i in n:
        sum = sum+int(i)**l
    if n==str(sum):
        print(f'{n} is a Armstrong number.')
    else:
        print(f"{n} is not a Armstrong number")
except:
    print("Enter a valid Integer number.")

# method 2 - using recurssion
try:
    m=input()
    l=len(m)
    def arm(o):
        if o>=l:
            return 0
        a=int(m[o])**l
        sum=a+arm(o+1)
        return sum
    if m==str(arm(0)):
        print(f"{m} is a Armstrong number.")
    else:
        print(f"{m} is not a Armstrong number.")
except:
    print("Enter a valid integer number.")

# emthod 3 - using modulus and floor division operator
try:
    s=int(input())
    n=s
    l=len(str(n))
    sum=0
    while n>0:
        a=(n%10)**l
        sum = sum + a
        n=n//10
    if s == sum:
        print(f"{s} is a Armstrong number.")
    else:
        print(f"{s} is not a Armstrong number.")
except:
    print("Enter a valid number.")

# method 4 - using function based approach

def is_arm_strong(num):
    num_len = 0
    while (num // 10 > 0):
        num_len = num_len + 1

    sum_od_digit = 0

    while (num > 0):
        sum_od_digit = sum_od_digit + ((num % 10)**num_len)
        num = num // 10

    return sum_od_digit

try:
    while(True):

        num = int(input("Enter a positive integer value : "))

        if (num <= 0):
            print("Enter positive Integer value")
        else:
            result = is_arm_strong(num)

            if(result == num):
                print(f"{num} is a armstrong number")
            else:
                print("Not a armstrong number")

        choice = input("Do you want to continue the program? (y/n) : ")
        if (choice.lower() == 'n'):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid input : {e}")

except Exception as e:
    print(f"Exception caught : {e}")




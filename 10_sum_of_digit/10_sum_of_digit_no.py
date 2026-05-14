# python program to find sum of digits of a numbers

# method 1 - using type casting
try:
    n=int(input("Enter number :"))
    sum=0
    for i in str(n):
        sum=sum+int(i)
    print(sum)
    pass
except:
    print("Enter valid numeric value")

# method 2 - using modulus operator
try:
    q=int(input("Enter number :"))
    sum=0
    while q>0:
        a=q%10
        sum=sum+a
        q=q//10
    print(sum)
except:
    print("Enter valid numeric value.")

# method 3 - using recurssion
try:
    n=int(input("Enter number :"))
    def sum(n):
        if n<=0:
            return 0
        a=n%10
        summ=a+sum(n//10)
        return summ
    print(sum(n))
except:
    print("Enter valid numeric value.")

# method 4 - using function based approach

def sum_of_digit(num):
    sum_ = 0
    for i in str(num):
        sum_ = sum_ + int(i)
    return sum_

try:
    while True:
        num = int(input("Enter a integer value : "))
        if (num <= 0):
            print("Enter a positive integer value")
        else:
            result = sum_of_digit(num)
            print(f"Sum of digit of {num} is {result}")
        
        choice = input("Do you want to continue the program? (y/n) : ")
        if (choice.lower() == 'n'):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except Exception as e:
    print(f"Exception caught : {e}")



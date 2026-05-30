# python program to check whether number is a perfect number or not
# perfect number - a number is a perfect number if the sum of its factors is equal to number itself

# method 1 - using iterations
try:
    n=int(input("Enter the number :"))
    sum=0
    for i in range(1,n//2+1):
        if n%i == 0:
                sum = sum+i
    if sum==n:
        print(f'{n} is a perfect number.')
    else:
        print(f'{n} is not a perfect number.')
except:
     print("Enter a valid integer value.")

# method 2 - using recursion
try:
    m=int(input("Enter number :"))
    sum=0
    def perfect_number(n):
        if n==m:
            return print(end="")
        global sum
        if m%n == 0:
            sum=sum+n
        perfect_number(n+1)
    perfect_number(1)
    if sum==m:
        print(f'{m} is a perfect number.')
    else:
        print(f'{m} is not a perfect number.')
except:
    print("Enter a valid integer value")

# method 3 - using module based approach

def isPerfect(num):
    summ = 0
    for i in range(1, num):
        if (num % i == 0):
            summ = summ + i
    if (summ == num):
        return True
    return False

try:
    while(True):
        num = int(input("Enter positive integer value : "))
        limit  = 1000
        if (num <= 0):
            print("Enter positiveinteger value")
        elif (num > limit):
            print("Input too large")
        else:
            result = isPerfect(num)
            if(result):
                print(f"{num} is a Perfect number")
            else:
                print(f"{num} is not a perfect number")
        
        choice = input("Do you want to continue the program (y/n) : ")
        if (choice.lower() == "n"):
            print("Program Finiched!")
            break

except ValueError as e:
    print(f"Invalid input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")


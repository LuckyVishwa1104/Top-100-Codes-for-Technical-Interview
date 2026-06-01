# python program to check whether a number is a Harshed number or not
# harshad number - a number which is completely divisible by the sum of digit of the number is called harshad number

# method 1 - using iteration
try:
    n=int(input("Enter the number :"))
    l=n
    sum=0
    for i in range(len(str(n))):
        n1=n%10
        n=n//10
        sum=sum+n1
    if l%sum == 0:
        print("It is a Harshad number")
    else:
        print("It is not a Harshad number")
except:
    print("Enter a valid integer value")

# method 2 - using recursion
try:
    n=int(input("Enter the number :"))
    sum=0
    def harshad_number(n):
        if n==0:
            return print(end="")
        n1=n%10
        global sum
        sum=sum+n1
        harshad_number(n//10)
    harshad_number(n)
    if n%sum == 0:
        print("Harshad number")
    else:
        print("Not a Harshad number")
except:
    print("Enter a valid integer value")

#method 4 - module based approach

def isHarshed(num):
    summ = 0
    numerator = num
    while num > 0:
        summ = summ + (num % 10)
        num = num // 10
    if (numerator % summ == 0):
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
            result = isHarshed(num)
            if(result):
                print(f"{num} is a Harshed number")
            else:
                print(f"{num} is not a Harshed number")
    
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

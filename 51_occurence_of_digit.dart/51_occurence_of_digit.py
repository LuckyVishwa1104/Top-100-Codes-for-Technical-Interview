# Python program to find the occurence of a particular digit in a number.

# Method 1 - using brut-force and iteration
try:
    n=int(input("Enter the number :"))
    m=int(input("Enter the digit :"))
    cnt=0
    while n>0:
        a=n%10
        if a==m:
            cnt+=1
        n=n//10
    print(cnt)
except:
    print("Enter a valid input value.")

# method 2 - using string data-type
try:
    n=input("Enter the number :")
    m=input("Enter the digit :")
    cnt=0
    for i in n:
        if i==m:
            cnt+=1
    print(cnt)
except:
    print("Enter a valid input value.")

# method 3 - using built-in method
try:
    n=input("Enter the number :")
    m=input("Enter the digit :")
    print(n.count(m))
except:
    print("Enter a valid input value.")
    
# method 4 - using module based approach

def digit_count(number, digit):
    count = 0
    while number > 0:
        a = number % 10
        if (a == digit):
            count += 1
        number //= 10
    return count

try:
    while (True):
        
        number = int(input("Enter month : "))
        digit = int(input("Enter year : "))

        if(digit < 0):
            print("Enter positive value for Digit")

        else:
            result = digit_count(number, digit)
            print(f"{digit} occurs {result} times in {number}")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice.lower() == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")


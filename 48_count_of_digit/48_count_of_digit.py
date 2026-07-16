# Python progrsm to count the numebr the digit in a particular number

# method 1 - using modulus operator and brut force
try:
    n=int(input("Enter the number :"))
    cnt=0
    while n>0:
        n=n//10
        cnt=cnt+1
    print(cnt)
except:
    print("Enter a valid input.")

# method 2 - using len() method
try:
    n=int(input("Enter the number :"))
    print(len(str(n)))
except:
    print("Enter a valid input.")

# method 3 - using recursion
try:
    n=int(input("Enter the number :"))
    cnt=1
    def digit_count(a):
        if a==0:
            return print(end="")
        global cnt
        cnt+=1
        digit_count(a//10)
    digit_count(n//10)
    print(cnt)
except:
    print("Enter a valid input.")

# method 4 - using module based approach

def digit_count(num):
    if (0 == num):
        return 1
    cnt = 0
    while num > 0:
        cnt+=1
        num//=10
    return cnt

try:
    while (True):
        
        num = int(input("Enter number : "))

        if(num < 0):
            num *= -1

        result = digit_count(num)
        print(f"No of digit in {num} ===> {result}")

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

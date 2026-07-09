# Python program to replace all Zeros with ones

# method 1 - using built-in methods
try:
    n=int(input("Enter the number :"))
    a=str(n).replace("0","1")
    print(a)
except:
    print("Enter a valid integer value!!!")

# method 2 - using brut force
try:
    n=int(input("Enter the number :"))
    s=list(str(n))
    for i in range(len(s)):
        if s[i]=="0":
            s[i]="1"
    print("".join(s))
except:
    print("Enter a valid integer value!!!")

# method 3 - using recurssion
try:
    n=int(input("Enter teh number :"))
    s=list(str(n))
    def func(a):
        if a>=len(s):
            return print(end="")
        if s[a]=="0":
            s[a]="1"
        func(a+1)
    func(0)
    print("".join(s))
except:
    print("Enter a valid integer value!!!")

# method 4 - using module based approach

def replace_zeros(num):
    if (num == 0):
        return 1
    place = 1
    result = 0
    while (num > 0):
        digit = num % 10 # extracting last digit for operation
        if (digit == 0):
            digit = 1
        result += (place * digit)
        place *= 10 # calculating digit's place on each iteration
        num //= 10 # updating num with remaing digit except last digit
    return result

try:
    while (True):
        num = int(input("Enter a Integer value: "))
    
        result = replace_zeros(abs(num))
        if (num < 0):
            print(f"{num} ===> {result * -1}")
        else:
            print(f"{num} ===> {result}")

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






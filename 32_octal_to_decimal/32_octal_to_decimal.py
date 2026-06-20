# Python program to convert octal to decimal

# method 1 - brut-force and iteration
try:
    n=int(input("Enter the Octal number :"))
    st=str(n)[::-1]
    sum=0
    for i in range(len(st)):
        a=int(st[i])*(8**(i))
        sum=sum+a
    print(sum)
except:
    print("Enter a valid integer value.")

# method 2 - using recursion
try:
    n=int(input("Enter the Octal number :"))
    sum=0
    stt=str(n)[::-1]
    def oct_to_dec(p):
        if p>=len(stt):
            return print(end="")
        a=int(stt[p])*(8**(p))
        global sum
        sum=sum+a
        oct_to_dec(p+1)
    oct_to_dec(0)
    print(sum)
except:
    print("Enter a valid integer value.")

# method 3 - using built-in function
try:
    n=int(input("Enter the octal number :"))
    octl=int(str(n),8)
    print(octl)
except:
    print("Enter a valid integer value.")

# method 4 - using module based approach

def octal_to_decimal(octal):
    pow = 0
    decimal_sum = 0
    for i in str(octal)[::-1]:
        decimal_sum = decimal_sum + (int(i) * (8 ** pow))
        pow+=1
    return decimal_sum

def is_valid_octal(num):
    for i in str(num):
        if i not in [0,1,2,3,4,5,6,7]:
            return False
    return True

try:
    while(True):
        num = int(input("Enter positive integer value : "))
        if (num < 0):
            print("Please enter a valid octal number.")
        elif (is_valid_octal(num)):
            print("Invalid octal number")
        else:
            result = octal_to_decimal(num)
            print(f"Octal {num} = {result} Decimal")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")



# Python program to convert decimal to binary

# method 1 - using brut-force(mind and sense) and iteration
try:
    n=int(input("Enter the decimal number :"))
    string=""
    while n>0:
        a=n%2
        n=n//2
        string=string+str(a)
    print((string)[::-1])
except:
    print("Enter the valid integer value")

# method 2 - using recursion
try:
    n=int(input("Enter the number :"))
    srt=""
    def func(n):
        if n<=0:
            return print(end="")
        s=n%2
        global srt
        srt=srt+str(s)
        func(n//2)
    func(n)
    print(srt[::-1])
except:
    print("Enter the valid integer value")

# method 3 - using built-in method
try:
    n=int(input("Enter the number :"))
    print(bin(n))
except:
    print("ENter a valid interger vaLUE")
    
# method 4 - using module based approach

def decimal_to_binary(decimal):
    binary_num = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary_num = binary_num + str(remainder)
    return binary_num[::-1]

try:
    while (True):
        num = int(input("Enter positive integer value : "))

        if (num < 0):
            print("Enter valid decimal number")
        else:
            result = decimal_to_binary(num)
            print(f"Decimal {num} = {result} Binary")

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



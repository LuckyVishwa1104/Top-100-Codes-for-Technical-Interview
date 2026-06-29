# Python program to convert to decimal to octal

# method 1 - using brut force and iterations
try:
    n=int(input("Enter the decimal number :"))
    srt=""
    while n>0:
        a=n//8
        b=n/8
        c=b-a
        srt=srt+str(int(c*8))
        n=a
        pass
    print(srt[::-1])
except:
    print("Enter a valid integer value!")

# method 2 - using recursion
try:
    n=int(input("Enter the decimal number :"))
    srt=""
    def func1(n):
        if n<=0:
            return print(end="")
        a=n//8
        b=n/8
        c=b-a
        global srt
        srt=srt+str(int(c*8))
        func1(a)
    func1(n)
    print(srt[::-1])
except:
    print("ENter a valid interger vaLUE")

# method 3 - using built-in function
try:
    n=int(input("Enter the decimal number :"))
    print(oct(n))
except:
    print("ENter a valid interger vaLUE")

# method 4 - using module based appoach

def decimal_to_octal(decimal):
    octal_num = ""
    while (decimal > 0):
        remainder = decimal % 8
        decimal = decimal // 8
        octal_num = octal_num + str(remainder)
    return octal_num[::-1]

try:
    while (True):
        num = int(input("Enter positive integer value : "))

        if (num < 0):
            print("Enter valid octal number")
        else:
            result = decimal_to_octal(num)
            print(f"Octal {num} = {result} Binary")

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

# method 5 - using module based approach

def decimal_to_hex(decimal):
    hex_map = {
    0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F",
    }

    hex_num = ""
    while decimal > 0:
        remainder = decimal % 16
        decimal = decimal // 16
        hex_num = hex_num + hex_map(remainder)
    return hex_num


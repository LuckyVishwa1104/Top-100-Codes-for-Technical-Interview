# Python program to convert Hexadecimal into decimal

# method 1 - using brut-force, list and iteration
try:
    n=input("Enter the Hexadecimal nunber :")
    list1=list(str(n)[::-1])
    if "A" in list1:
        list1[list1.index("A")]=10
    if "B" in list1:
        list1[list1.index("B")]=11
    if "C" in list1:
        list1[list1.index("C")]=12
    if "D" in list1:
        list1[list1.index("D")]=13
    if "E" in list1:
        list1[list1.index("E")]=14
    if "F" in list1:
        list1[list1.index("F")]=15
    sum=0
    for i in range(len(n)):
        a=int(list1[i])*(16**(i))
        sum=sum+a
    print(sum)
except:
    print("Enter a valid Numeric value.")

# method 2 - using ASCII value
try:
    m=input("Enter the number :")
    n=m[::-1]
    sum=0
    for i in range(len(n)):
        if "0"<=n[i]<="9":
            a=int(n[i])*(16**(i))
            sum=sum+a
        elif "A"<=n[i]<="F":
            a=(ord(n[i])-55)*(16**(i))
            sum=sum+a
    print(sum)
except:
    print("Enter a valid numeric value.")

# method 3 -using recursion function
try:
    m=input("Enter the number :")
    n=m[::-1]
    sum=0
    def hex_to_deci(i):
        if i>=len(m):
            return print(end="")
        global sum
        if "0"<=n[i]<="9":
            a=int(n[i])*16**(i)
            sum=sum+a
        if "A"<=n[i]<="F":
            a=(ord(n[i])-55)*16**(i)
            sum=sum+a
        hex_to_deci(i+1)
    hex_to_deci(0)
    print(sum)
except:
    print('Enter a valid numeric value')

# method 4 - using built-in function
try:
    n=input("Enter the number :")
    deci=int(n,16)
    print(deci)
except:
    print("Enter a valid numeric value.")

# method 5 - using module based approach

HEX_DIGITS = set(list("0123456789ABCDEFabcdef"))

def is_valid_hex_number(hex_num):
    for digit in str(hex_num):
        if digit not in HEX_DIGITS:
            return False
    return True

def hex_to_decimal(hex_num):
    hex_num_map = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
        "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15
    }
    rev_hex_num = str(hex_num)[::-1]
    decimal_number = 0
    for ch in rev_hex_num:
        # int(ch, 16) handles 0-9 and A-F

        decimal_number = decimal_number * 16 + int(ch, 16)
    return decimal_number

try:
    while(True):
        num = input("Enter positive integer value : ").strip()

        if num == "":
            print("Please enter a valid hex number.")
        elif not is_valid_hex_number(num):
            print("Invalid hex number")
        else:
            result = hex_to_decimal(num)
            print(result)

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



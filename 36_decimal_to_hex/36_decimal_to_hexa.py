# Python program to convert a decimal number into hexa-decimal number
# method 1 - using brut force and Iterations

# try:
#     n=int(input("Enter the decimal bunber"))
#     srt=""
#     while n>0:
#         a=n%16
#         if (0<=a<=9):
#             srt=srt+str(a)
#         elif (10<=a):
#             srt=srt+chr(a+55)
#         n=n//16
#     print(srt[::-1])
# except:
#     print("An error occured")

# # method 2 - using recursion
# try:
#     n=int(input("Enter the decimal number :"))
#     srt=""
#     def func1(n):
#         if n<=0:
#             return print(end="")
#         global srt
#         a=n%16
#         if (0<=a<=9):
#             srt=srt+str(a)
#         elif (10<=a):
#             srt=srt+chr(a+55)
#         func1(n//16)
#         pass
#     func1(n)
#     print(srt[::-1])
# except:
#     print("An error occured")

# # method 3 - using built-in method
# try:
#     n=int(input("Enter the decimal value :"))
#     print(hex(n))
# except:
#     print("An error occured")

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

    if decimal == 0:
        return 0

    hex_num = ""
    while decimal > 0:
        remainder = decimal % 16
        decimal = decimal // 16
        hex_num = hex_num + hex_map[remainder]
    return hex_num[::-1]

try:
    while (True):
        num = int(input("Enter positive integer value : "))

        if (num < 0):
            print("Enter valid decimal number")
        else:
            result = decimal_to_hex(num)
            print(f"Decimal {num} = {result} Hex")

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



# python program to check whether a number is a aotomorphic number or not
# Automorphic number - a number whose square ends with the number itself is called automorphic number

# # method 1 - using modulus opearator
# try:
#     n=int(input("Enter the number :"))
#     p=n
#     m=n**2
#     cnt=0
#     while n>0:
#         n=n//10
#         cnt=cnt+1
#     if p == m%(10)**cnt:
#         print(f'{p} is an Automorphic number.')
#     else:
#         print(f"{p} is not an Automorphic number.")
# except:
#     print("Enter the valid integer value")

# # method 2 - using endswith() method of string
# # endswith() - is a method of string, it return true value when a string end with the specified srting
# try:
#     n=int(input("Enter the number :"))
#     if str(n**2).endswith(str(n)):
#         print("Automorphic number")
#     else:
#         print("Not an Automorphic number.")
# except:
#     print("Enter the valid integer value")

# # method 3 - using slicing operator
# try:
#     n=int(input("Enter the number :"))
#     m=n**2
#     if str(n) == str(m)[-len(str(n))::]:
#         print("Automorphic number")
#     else:
#         print("Not an Automorphic number.")
# except:
#     print("Enter the valid integer value")


# method 4 - module based approach

def is_automorphic(num):
    num_square = num * num
    while (num > 0):
        if(num%10 != num_square%10):
            return False
        num = num // 10
    return True

try:
    while(True):

        num = int(input("Enter positive integer value : "))
        limit  = 1000
        if (num <= 0):
            print("Enter positiveinteger value")
        elif (num > limit):
            print("Input too large")
        else:
            result = is_automorphic(num)
            if (result):
                print(f"{num} is a automorphic number")
            else:
                print(f"{num} is not a automorphic number")

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


# python program to check whether the number is a perfect square or not
# a number is a perfect square if its root is an integer value.

# method 1 - checking equality of square
n=int(input("Enter a number :"))
m=int(n**(0.5))
if m**2 == n:
    print(f"{n} is a perfect square")
else:
    print(f"{n} is not a perfect square")

# method 2 - checking equality of root
n=int(input("Enter a number :"))
m=n**(0.5)
l=int(m)
if m == l:
    print(f"{n} perfect square")
else:
    print(f"{n} not a Perfect Square")

# method 3 - module based approach

def is_perfect_square(num):
    square_root = int(num ** (0.5))
    if (square_root * square_root):
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
            result = is_perfect_square(num)
            if(result):
                print(f"{num} is a perfect square")
            else:
                print(f"{num} is not a perfect square")

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

    
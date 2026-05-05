# program to check number is even or odd

# method 1
try:
    num=int(input())
    if num%2==0:
        print(f"{num} is a Even number")
    else:
        print(f"{num} is a Odd number")
except:
    print("Enter a valid number.")

# method 2 - using ternary operators
try:
    num=int(input())
    print("Even" if num%2==0 else "Odd")

    print("Even") if num%2==0 else print("Odd")

except:
    print("Enter valid number")


def evenOdd(no):
    try:
        num = int(no)
        if (num%2 == 0 and num != 0):
            print(f'{num} is even number.')
        elif (num%2 == 1):
            print(f'{num} is a odd number')
        else:
            print(f'Input is Zero')

    except:
        print('Enter a valid numeric input')

a = input('Enter a numeric value : ')
evenOdd(a)

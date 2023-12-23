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


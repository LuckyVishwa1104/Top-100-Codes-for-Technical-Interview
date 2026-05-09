# python program to check leap year or not

# method 1 - traditional method
try:
    a=int(input("Enter Year :"))
    if a%4==0 and a%100!=0:
         print(f"{a} is a Leap year.")
    elif a%400 == 0:
        print(f"{a} is a Leap year.")
    else:
        print(f'{a} is not a Leap year.')
except:
    print("Enter valid year.")

# method 2 - using ternary operator
try:
    a=int(input("Enter a year :"))
    print(f"{a} is a Leap year." if a%400==0 else f"{a} is a Leap year." if a%4==0 and a%100!=0 else f"{a} is not a Leap year.")
except:
    print("Enter a valid year.")

# method 3 - using calendar module
import calendar
try:
    a=int(input("Enter a Year :"))
    if calendar.isleap(a):
        print(f'{a} is a leap year.')
    else:
        print(f"{a} is not a leap year")
except:
    print("Enter valid Year.")


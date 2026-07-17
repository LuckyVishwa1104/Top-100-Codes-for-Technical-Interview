# Python program to find number of days in a particular month od particular year

# method 1 -using brut-force
m=int(input("Enter month :"))
y=int(input("Enter year :"))
if m==2 and ((y%4==0 or y%100==0) and y%400==0):
    print("Number of days is 29")
elif (m==2):
    print("NUmber of days is 28")
elif m in [1,3,5,7,8,10,12]:
    print("NUmber of days is 31")
else:
    print(print("NUmber of days is 30"))

# method 2 - using module based approach 

def no_of_days(month, year):
    if (month == 2 and ((year % 4 == 0 or year % 100 == 0) and year % 100 == 0)):
        return 29

    elif(month == 2):
        return 28
    
    elif (m in [1,3,5,7,8,10,12]):
        return 31
    
    else:
        return 30

try:
    while (True):
        
        month = int(input("Enter month : "))
        year = int(input("Enter year : "))

        if(month <= 0 or year <= 0):
            print("Enter positive Integer Value")
        
        elif (month > 12):
            print("Eeter a valid month.")

        else:
            result = no_of_days(month, year)
            print(f"{month} {year} has {result} days.")

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


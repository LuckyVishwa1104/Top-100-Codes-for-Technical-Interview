# Strong number - a number is a strong number if the sum of factorial of each digit in number is equal to number itself

# method 1 - using iteration
try:
    n=int(input("Enter the number :"))
    m=n
    sum=0
    while sum<m:
        n1=n%10
        n=n//10
        fac=1
        for i in range(1,n1+1):
            fac=fac*i
        sum=sum+fac     
    if sum==m:
        print(f"{m} is a Strong Number.")
    else:
        print(f"{m} is not a Strong Number.")
except:
    print("Enter a valid number.")

# method 2 - using recurssion
try:
    n2=int(input("Enter a number :"))
    sum=0
    def strong_number(n2):
        if n2==0:
            return print(end="")
        n1=n2%10
        def fac(n1):
            if n1==0:
                return 1
            facc=n1
            return facc*fac(n1-1)
        global sum
        sum=sum+fac(n1)
        strong_number(n2//10)
    strong_number(n2)
    if sum==n2:
        print(f"{n2} is a Strong number")
    else:
        print(f"{n2} is not a Strong number")
except:
    print("Enter a valid integer value")

# method 3 - using module based approach

def fac(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

def is_strong(num):
    strong_value = 0
    temp = num
    while num > 0:
        strong_value = strong_value + fac(num % 10)
        num = num // 10
    if (temp == strong_value):
        return True
    return False

try:
    while(True):
        num = int(input("Enter a integer value : "))
        if (num <= 0):
            print("Enter positiveinteger value")
        else:
            result = is_strong(num)
            if (result):
                print(f"{num} is a strong number")
            else:
                print(f"{num} is not a strong number")

        choice = input("Do you want to continue the program (y/n) : ")
        if (choice.lower() == "n"):
            print("Program Finiched!")
            break

except ValueError as e:
    print(f"Invalid input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")


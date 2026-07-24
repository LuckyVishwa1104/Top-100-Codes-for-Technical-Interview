# Python program to find whether a number is a prime or not using recursion

# method 1 - using recursion
try:
    n=int(input("Enter the number :"))
    def prime(a):
        if a==n:
            return print(f"{n} is a prime number.")
        if n%a==0:
            return print(f"{n} is not a prime number.")
        prime(a+1)
    prime(2)
except:
    print("Something went worng!!!")

# method 2 - using third variable
try:
    n=int(input("Enter the number :"))
    def prime(a):
        if a==n:
            return True
        if n%a==0:
            return False
        return prime(a+1)
    if prime(2):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
except:
    print("Something went worng!!!")

# method 3 - usign recursion and error-handling

try:
    while (True):
        number = int(input("Enter number : "))
        def prime(num):
            print(num)
            if (num >= number):
                return True
            if (number % num == 0):
                return False
            return prime(num + 1)
        
        result = prime(2)
        print(result)

        if(result):
            print(f"{number} is prime number")
        else:
            print(f"{number} is not prime number")
        
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


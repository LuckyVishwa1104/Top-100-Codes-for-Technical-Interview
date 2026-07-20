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
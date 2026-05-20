# python program to display FIBONACCI series upto nth number
# fibonacci series is a sequence of number for which every third number is the sum of previous two numbers

# method 1 - using simple iteratrion
try:
    n=int(input())
    n1=0
    print(n1)
    n2=1
    while n2<=n:
        print(n2)
        n3=n1+n2
        n1=n2
        n2=n3
except:
    print("Enter a valid number")

# method 2 - using recurssion
try:
    n=int(input())
    n1=0
    print(n1,end=" ")
    n2=1
    print(n2,end=" ")
    def fibb(n1,n2):
        n3=n1+n2
        n1=n2
        n2=n3
        if n2>n:
            return ""
        return str(n2)+" "+str(fibb(n1,n2))
    print(fibb(n1,n2))
except:
    print("Enter a valid integer value number.")

# method 3 - function based approach
def fibonacci_series(num):
    n1 = 0
    fibo_series = [n1]
    n2 = 1
    while (n2 <= num):
        fibo_series.append(n2)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return fibo_series

try:
    while(True):
        num = int(input("Enter range value : "))
        if (num <= 1):
            print("Enter integer value greater than 1")
        else:
            result = fibonacci_series(num)
            print(result)

        choice = input("Do you want to continue the program? (y/n) : ")
        if (choice.lower() == 'n'):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except Exception as e:
    print(f"Exception caught : {e}")



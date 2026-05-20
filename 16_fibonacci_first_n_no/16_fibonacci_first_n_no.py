# program to display fibonacci series upto first n numbers.

# method 1 - using simple iteration
try:
    n=int(input("Enter the number :"))
    n1=0
    print(n1)
    n2=1
    for i in range(n-1):
        print(n2)
        n3=n1+n2
        n1=n2
        n2=n3
except:
    print("Enter a valid integer value")

# method 2 - using recurssion
try:
    n=int(input())
    n1=0
    print(n1,end=" ")
    n2=1
    print(n2,end=" ")
    cnt=0
    def fibb(n1,n2):
        global cnt
        cnt=cnt+1
        n3=n1+n2
        n1=n2
        n2=n3
        if cnt>n-2:
            return ""
        return str(n2)+" "+str(fibb(n1,n2))
    print(fibb(n1,n2))
except:
    print('Enter a valid integer value.')

# method 3 - using function based approach

def fibonacci_series(num):
    n1 = 0
    n2 = 1
    fibo_series = [n1]
    
    for i in range(num+1):
        fibo_series.append(n2)
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    return fibo_series

try:
    while (True):
        num = int(input("Enter positive integer number : "))

        if(num < 0):
            print("Enter positive integer value")

        else:
            result = fibonacci_series(num)
            print(result)

except ValueError as e:
    print("Invalid Input : {e}")

except Exception as e:
    print("Exception caught : {e}")
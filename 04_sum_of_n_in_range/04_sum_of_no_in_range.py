# python program to find sum of numbers in provided range
# method 1 - traditional way
try:
    m,n=map(int,input().split(','))
    sum=0
    for i in range(m,n+1):
        sum=sum+i
    print(sum)
except:
    print("Enter valid range i.e. from starting to ending n,m")

# method 2 - using recurssion
try:
    m,n=map(int,input().split(','))
    def sum(m,n):
        if m>n:
            return 0
        summ=m+sum(m+1,n)
        return summ
    print(sum(m,n))
except:
    print("Enter valid range i.e. from starting to ending n,m")

# method 3 - function based approach

def sumation(start, end):
    end = end + 1
    sum = 0
    for i in range (start, end):
        sum = sum + i
    return sum

try:
    a = int(input("Enter starting range : "))
    b = int(input("Enter ending range : "))
    if (a < 0 or b < 0):
        print("Enter positive integer value")
    else:
        c = sumation(a, b)
        print(f"Sum of range between {a} and {b} : {c}")

except ValueError as e:
    print(f"Invalid Input format : {e}")

except IndexError as e:
    print(f"Index out of Range : {e}")

except Exception as e:
    print(f"Exception caught : {e}")


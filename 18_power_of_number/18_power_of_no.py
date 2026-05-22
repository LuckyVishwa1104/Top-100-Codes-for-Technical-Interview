# python program to find the power of a number

# method 1 - using the operator
try:
    n=eval(input("Enter the number :"))
    m=int(input("Enter the power term :"))
    pow=n**m
    print(round(pow,4))
except:
    print('ENter a valid Integer value!')

# method 2 - using simple iteration
try:
    n=eval(input("Enter the number :"))
    m=int(input("Enter the power term :"))
    pow=1
    for i in range(m):
        pow=pow*n
    print(round(pow,4))
except:
    print("Enter a valid integer value!")

# method 3 - using recurssion
try:
    n=int(input("Enter a number :"))
    m=int(input("Enter a power term :"))
    def pow(a,b):
        if b==0:
            return 1
        return a*pow(a,b-1)
    print(pow(n,m))
except:
    print("Enter a valid integer value!")

# method 4 - using function based approach 

def power_of_number(num, pow):
    result = 1
    for i in range(1,pow+1):
        result = result * num
    return result

try:
    num = int(input("Enter number : "))
    pow = int(input("Enter power factor : "))
    if (num <= 0 or pow <= 0):
        print("Enter a positive value")
    else:
        result = power_of_number(num,  pow)
        print(result)

except ValueError as e:
    print("Invalid Input : {e}")

except Exception as e:
    print("Exception caught : {e}")



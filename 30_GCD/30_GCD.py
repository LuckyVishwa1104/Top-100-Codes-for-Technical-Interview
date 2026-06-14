# Pyhton program to find GCD of a given number
# GCD - greatest common divisor is the largest common number that completely divides the given two numbers

# method 1 - using iteration
a,b=map(int,input("Enter two space separate numbers :").split(" "))
for i in range(min(a,b)):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

# method 2 - using recursion
a,b=map(int,input("Enter two space separate numbers :").split(" "))
def fun1(i):
    if i>min(a,b):
        return print(end="")
    if a%i==0 and b%i==0:
        global gcd
        gcd=i
    fun1(i+1)
fun1(1)
print(gcd,"is the GCD")

# method 3 - using module based approach

def gdc(num1, num2):
    minn = min([num1,num2])
    for i in range(1, minn + 1):
        if (num1%minn and num2%minn):
            return minn

try:
    while(True):
        num1 = int(input("Enter positive integer value : "))
        num2 = int(input("Enter positive integer value : "))
        limit  = 1000
        if (num1 == 0 or num2 == 0):
            print("Enter positive integer value")
        elif (num1 > limit or num2 > limit):
            print("Input too large")
        else:
            result = gdc(num1, num2)
            print(f"GCD = {result}")
    
        choice = input("Do you want to continue the program (y/n) : ")
        if(choice == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print("Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")
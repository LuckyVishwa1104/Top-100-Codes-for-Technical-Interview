# Python program to fing highest common factor of two numbers
# HCF - hcf is a number highest number that conbinely divides both the numbers

# method 1 - using Iteration
a,b=map(int,input("Enter the two space separated numbers :").split(" "))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
print(f"{hcf} is the HCF")

# method 2 - using recursion
a,b = map(int,input("Enter two space separated number :").split())
def hcf_fun(i):
    if i>min(a,b):
        return print(end="")
    if a%i==0 and b%i==0:
        global hcf
        hcf=i
    hcf_fun(i+1)
hcf_fun(1)
print(hcf,"is HCF")

# method 4 - using module based approach

def hcf(num1, num2):
    end = min([num1,num2])
    common_factor = []
    for i in range (1, end+1):
        if (num1%i==0 and num2%i==0):
            common_factor.append(i)
    return max(common_factor)

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
            result = hcf(abs(num1), abs(num2))
            print(f"HCF - {result}")

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

# method 5 - euclidean algorothm

def euclidean_hfc(num1, num2):
    while num2 > 0:
        temp = num1
        num1 = num2
        num2 = temp % num2
    return num1

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
            result = euclidean_hfc(abs(num1), abs(num2))
            print(f"HCF - {result}")

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


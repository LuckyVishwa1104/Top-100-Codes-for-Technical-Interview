# python program to find prime factorials of a numbers
# factor - factores of a number are the numbers which completely divides the number

# method 1 - using iterations
try:
    n=int(input("Enter the number :"))
    for i in range(2,n+1):
        if n%i==0:
            for j in range(2,(i//2)+1):
                if i%j==0:
                    break
            else:
                print(i)
except:
    print("Enter a valid integer values!")

# following recursion will iterate only upto 1000 times due to default value, hence it will provide result for upto 1000 number as input
# to increse the limit following code is used
import sys
sys.setrecursionlimit(2000)  # it  will set the recursion limit to 2000 iterations

# method 2 - using recurssion
l=int(input('Enter Number :'))
if l%2==0:
    print(2)
def p_fac(n):
    if n>l:
        return print(end="")
    if l%n==0:    
        def prm(p,k1=n): 
            if k1%p==0:
                return print(end="")
            if p==k1-1:
                return print(k1)
            prm(p+1)
        prm(2)
    p_fac(n+1)
p_fac(2)

# method 3 - using function based approach

def is_prime(num):
    for i in range(2, (num // 2) + 1):
        if (num % i == 0):
            return False
    return True

def prime_factor(num):

    factor_list = [i for i in range (2, (num // 2) + 1) if (num % i == 0)]

    factor_list.append(num)

    # for i in range(2, (num // 2) + 1):
    #     if (num % i == 0):
    #         factor_list.append(i)
    
    prime_factor_list = [ i for i in factor_list if is_prime(i) == True]

    # for i in factor_list:
    #     if is_prime(i) == True:
    #         prime_factor.append(i)

    return prime_factor_list

try:
    while(True):
        num = int(input("Enter a positive integer value : "))
        max_limit = 10000

        if (num > max_limit):
            print("Input to large")
        elif (num <= 0):
            print("Enter a positive integer value.")
        else:
            resutl = prime_factor(num)
            print(resutl)

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print("Invalid Input : {e}")

except Exception as e:
    print("Exception caught : {e}")


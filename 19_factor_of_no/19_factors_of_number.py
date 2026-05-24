# python program to find factors of a number
# factor of a number are the nunmbers that can divide the given number perfectly

# method 1 - using simple iteration 
try:
    n=int(input("Enter the number :"))
    if n<0:
        print("Enter number greater than or equal to Zero")
    else:
        for i in range(1,(n//2)+1):
            if n%i==0:
                print(i,end=" ")
        print(n)
except:
    print("Enter a valid integer value!")

# method 2 - using recurssion
try:
    n=int(input("Enter number :"))
    def fac(a):
        if a>n//2:
            return print(n)
        if n%a==0:
            print(a,end=' ')
        fac(a+1)
    fac(1)
except:
    print("Enter a valid integer value!")

# method 2 - using module based approach

def factor_of_no(num):
    factor_list = [1]
    for i in range(2, (num //2 + 1)):
        if (num % i == 0):
            factor_list.append(i)
    if (num != 1):
        factor_list.append(num)
    return factor_list

try:
    while(True):
        num = int(input("Enter a positive integer value : "))
        max_limit = 10000

        if (num > max_limit):
            print("Input to large")
        elif (num <= 0):
            print("Enter a positive integer value.")
        else:
            resutl = factor_of_no(num)
            print(resutl)

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print("Invalid Input : {e}")

except Exception as e:
    print("Exception caught : {e}")

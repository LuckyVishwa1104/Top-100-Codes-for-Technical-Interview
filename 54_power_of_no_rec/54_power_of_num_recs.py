# Python program to find power of a number using recursion

# method 1 - using recursion
try:
    n=int(input("Enter the number :"))
    m=int(input("Enter the power number :"))
    pro=1
    def powr(a):
        if a>m:
            return
        global pro
        pro=pro*n
        powr(a+1)
    powr(1)
    print(pro)
except:
    print("Something went wrong!!!")

# method 2 - 
try:
    n=int(input("Enter the number :"))
    m=int(input("Enter the power number :"))
    def fac(n,m):
        if m==0:
            return 1
        return n*fac(n,m-1)
    print(fac(n,m))
except:
    print("Something went wrong!!!")

# method 3 - using module based approach

try:
    while (True):
        
        number = int(input("Enter number : "))
        pow = int(input("Enter power factor : "))

        result = 1
        def pow(num):
            if (num > pow):
                return
            global result
            result *=  number
            pow(num + 1)
        pow(1)

        print(f"{number} ^ {pow} = {result}.")

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


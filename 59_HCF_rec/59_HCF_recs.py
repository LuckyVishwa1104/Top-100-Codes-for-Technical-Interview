# python program to find HCF of a number

# method 1 - using recursion
try:
    num1=int(input("Enter the first nunmber :"))
    num2=int(input("Enter the second number :"))
    hcf=1
    def func1(a):
        if a>min(num1,num2):
            return
        if num1%a==0:
            def func2(b):
                if b>min(num1,num2):
                    return
                if num2%b==0:
                    if a==b:
                        global hcf
                        hcf=a
                func2(b+1)
            func2(2)
        func1(a+1)
    func1(2)
    print(hcf)
except:
    print("Something went wrong!!!")

# method 2 - using efficeint way
try:
    n,m=map(int,input().split())
    # hcf=1
    def func(a):
        if a>min(n,m):
            return
        if n%a==0 and m%a==0:
            global hcf
            hcf=a
        func(a+1)
    func(1)
    print(hcf)
except:
    print("Something went wrong!!!")

# method 3 - using exception and module based approach

try:
    while(True):

        num1 = int(input("Enter positive integer value : "))
        num2 = int(input("Enter positive integer value : "))
        limit  = 1000

        def eucledian_hcf(a):
            if (a <= 0): return
            global num1
            temp = num1
            num1 = a
            eucledian_hcf(temp % a)

        if (num1 == 0 or num2 == 0):
            print("Enter positive integer value")
        elif (num1 > limit or num2 > limit):
            print("Input too large")
        else:
            eucledian_hcf(min(num2,num1))
            print(f"HCF - {num1}")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice.lower() == "n"):
            print("Program finished!")
            break

except ValueError as ve:
    print(f"Invalid input - {ve}")

except ZeroDivisionError as zde:
    print(f"Zero Division Exception - {zde}")

except Exception as e:
    print(f"Exception caught - {e}")

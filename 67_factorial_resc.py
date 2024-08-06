# Python program to find factorial of a number using recursion

# method 1 - using recursion
try:
    num = int (input("Enter the number :"))
    fac=1
    def function1(a):
        if a> num:
            return
        global fac
        fac=fac*a
        function1(a+1)
        pass
    function1(1)
    print(fac)
except:
    print("Enter a valid input .")

# method 2 - using iteration
try:
    num1 = int(input("Enter the number :"))
    fac1 = 1
    i=1
    while i<=num:
        fac1 = fac1*i
        i+=1
    print(fac1)
except:
    print("Enter a valid input .")

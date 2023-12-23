# Python program to convert a decimal number into hexa-decimal number
# method 1 - using brut force and Iterations

try:
    n=int(input("Enter the decimal bunber"))
    srt=""
    while n>0:
        a=n%16
        if (0<=a<=9):
            srt=srt+str(a)
        elif (10<=a):
            srt=srt+chr(a+55)
        n=n//16
    print(srt[::-1])
except:
    print("An error occured")

# method 2 - using recursion
try:
    n=int(input("Enter the decimal number :"))
    srt=""
    def func1(n):
        if n<=0:
            return print(end="")
        global srt
        a=n%16
        if (0<=a<=9):
            srt=srt+str(a)
        elif (10<=a):
            srt=srt+chr(a+55)
        func1(n//16)
        pass
    func1(n)
    print(srt[::-1])
except:
    print("An error occured")

# method 3 - using built-in method
try:
    n=int(input("Enter the decimal value :"))
    print(hex(n))
except:
    print("An error occured")

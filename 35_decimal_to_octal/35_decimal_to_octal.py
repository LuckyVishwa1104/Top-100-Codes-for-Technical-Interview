# Python program to convert to decimal to octal

# method 1 - using brut force and iterations
try:
    n=int(input("Enter the decimal number :"))
    srt=""
    while n>0:
        a=n//8
        b=n/8
        c=b-a
        srt=srt+str(int(c*8))
        n=a
        pass
    print(srt[::-1])
except:
    print("Enter a valid integer value!")

# method 2 - using recursion
try:
    n=int(input("Enter the decimal number :"))
    srt=""
    def func1(n):
        if n<=0:
            return print(end="")
        a=n//8
        b=n/8
        c=b-a
        global srt
        srt=srt+str(int(c*8))
        func1(a)
    func1(n)
    print(srt[::-1])
except:
    print("ENter a valid interger vaLUE")

# method 3 - using built-in function
try:
    n=int(input("Enter the decimal number :"))
    print(oct(n))
except:
    print("ENter a valid interger vaLUE")
    
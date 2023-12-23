# Python program to convert decimal to binary

# method 1 - using brut-force(mind and sence) and iteration
try:
    n=int(input("Enter the decimal number :"))
    string=""
    while n>0:
        a=n%2
        n=n//2
        string=string+str(a)
    print((string)[::-1])
except:
    print("Enter the valid integer value")

# method 2 - using recursion
try:
    n=int(input("Enter the number :"))
    srt=""
    def func(n):
        if n<=0:
            return print(end="")
        s=n%2
        global srt
        srt=srt+str(s)
        func(n//2)
    func(n)
    print(srt[::-1])
except:
    print("Enter the valid integer value")

# method 3 - using built-in method
try:
    n=int(input("Enter the number :"))
    print(bin(n))
except:
    print("ENter a valid interger vaLUE")
    
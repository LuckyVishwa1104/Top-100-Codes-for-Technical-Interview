# Python program to convert octal to decimal

# method 1 - brut-force and iteration
try:
    n=int(input("Enter the Octal number :"))
    st=str(n)[::-1]
    sum=0
    for i in range(len(st)):
        a=int(st[i])*(8**(i))
        sum=sum+a
    print(sum)
except:
    print("Enter a valid integer value.")

# method 2 - using recursion
try:
    n=int(input("Enter the Octal number :"))
    sum=0
    stt=str(n)[::-1]
    def oct_to_dec(p):
        if p>=len(stt):
            return print(end="")
        a=int(stt[p])*(8**(p))
        global sum
        sum=sum+a
        oct_to_dec(p+1)
    oct_to_dec(0)
    print(sum)
except:
    print("Enter a valid integer value.")

# method 3 - using built-in function
try:
    n=int(input("Enter the octal number :"))
    octl=int(str(n),8)
    print(octl)
except:
    print("Enter a valid integer value.")
    
# Python program to replace all Zeros with ones

# method 1 - using built-in methods
try:
    n=int(input("Enter the number :"))
    a=str(n).replace("0","1")
    print(a)
except:
    print("Enter a valid integer value!!!")

# method 2 - using brut force
try:
    n=int(input("Enter the number :"))
    s=list(str(n))
    for i in range(len(s)):
        if s[i]=="0":
            s[i]="1"
    print("".join(s))
except:
    print("Enter a valid integer value!!!")

# method 3 - using recurssion
try:
    n=int(input("Enter teh number :"))
    s=list(str(n))
    def func(a):
        if a>=len(s):
            return print(end="")
        if s[a]=="0":
            s[a]="1"
        func(a+1)
    func(0)
    print("".join(s))
except:
    print("Enter a valid integer value!!!")
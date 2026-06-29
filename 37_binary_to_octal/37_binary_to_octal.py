# Python program to convert binary number to octal 

# method 1 - brute-force and iteration

try:
    n=int(input("Enter the binary number :"))
    oct=""
    while n>0:
        a=n%1000
        s=str(a)[::-1]
        sum=0
        for i in range(len(s)):
            if int(s[i]) == 1:
                sum=sum+2**(i)
        oct=oct+str(sum)
        n=n//1000
    print(oct)
except:
    print("Enter a valid integer value!!!")

# method 2 - using built-int methods
try:
    n=int(input("Enter the binary number :"))
    octl=oct(int(str(n),2))
    print(octl)
except:
    print("Enter a valid integer value!!!")

# method 3 - using recursion
try:
    n=int(input("Enter the binary number :"))
    octl=""
    def binary_to_actal(n):
        if n<=0:
            return print(end="")
        a=n%1000
        summ=0
        s=str(a)[::-1]
        def bin_three(i):
            if i>=len(s):
                return print(end="")
            
            if int(s[i])==1:
                nonlocal summ
                summ = summ + 2**(i)
            # print(summ)
            bin_three(i+1)
        bin_three(0)
        # print(summ)
        global octl
        octl=octl+str(summ)
        binary_to_actal(n//1000)
    binary_to_actal(n)
    print(octl)
except:
    print('Some issue occured!!!')

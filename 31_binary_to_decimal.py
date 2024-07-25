# python program to convert binary number into integer or decimal.

# emthod 1 - using brut force and iterations
try:
    n=int(input("Enter the Binary number :"))
    m=str(n)[::-1]
    sum=0
    for i in range(0,len(m)):
        if int(m[i])==1:
            sum=sum+2**(i)
    print(sum)
except:
    print("Enter a valid integer value.")

# method 2 - using bubilt-in funciton
# int(num,2) - this function is used to convert binary input into decimal value
# it accept two parameters first is the number in string data-type and second is the identifier(2 - for binary, 8 - for octal, 16 - for hexa-decimal)

try:
    n=int(input("Enter the binary number :"))
    deci=int(str(n),2)
    print(deci)
except:
    print("Enter a valid integer value.")

# method 3 - using recurssion
try:
    m=int(input("Enter the binary number :"))
    st=str(m)[::-1]
    sum=0
    def bin_to_oct(n):
        if n>=len(st):
            return print(end="")
        if int(st[n]) == 1:
            global sum
            sum=sum+2**(n)
        bin_to_oct(n+1)
    bin_to_oct(0) 
    print(sum)   
except:
    print("Enter a valid integer value.")

# Python program to convert octal number into its equvalent binary number

# method 1 - brut-force
import sys
n=int(input("Enter the octal number :"))
bina=""
def octal_to_binary(n):
    if n<=0:
        return print(end="")
    a=n%10
    srt=""
    def binary(a,j):
        if j>=3:
            return print(end="")
        m=a%2
        nonlocal srt
        srt=str(m)+srt
        binary(a//2,j+1)
        pass
    binary(a,0)
    global bina
    bina=srt+bina
    octal_to_binary(n//10)
    pass
octal_to_binary(n)
print(int(bina))


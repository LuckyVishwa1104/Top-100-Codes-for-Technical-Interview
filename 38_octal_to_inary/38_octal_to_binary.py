# Python program to convert octal number into its equvalent binary number

# method 1 - using brut-force
n=int(input("Enter the octal unmber :"))
octl=""
while n>0:
    a=n%10
    j=0
    srt=""
    while j<3:
        b=a%2
        srt=str(b)+srt
        j=j+1
        a=a//2
    octl=srt+octl
    n=n//10
print(int(octl))

# method 2 - using recursion
# import sys
# n=int(input("Enter the octal number :"))
# bina=""
# def octal_to_binary(n):
#     if n<=0:
#         return print(end="")
#     a=n%10
#     srt=""
#     def binary(a,j):
#         if j>=3:
#             return print(end="")
#         m=a%2
#         nonlocal srt
#         srt=str(m)+srt
#         binary(a//2,j+1)
#         pass
#     binary(a,0)
#     global bina
#     bina=srt+bina
#     octal_to_binary(n//10)
#     pass
# octal_to_binary(n)
# print(int(bina))

# method 3 - using built-in method
n=int(input("Enter the octal number :"))
bina=bin(int(n,8))
print(bina)
# srt=''
# for i in range(1,11):
#     srt=srt+str(i)
# print(srt)

# srtt=''
# for i in range(1,11):
#     srtt=str(i)+srtt
# print(srtt)

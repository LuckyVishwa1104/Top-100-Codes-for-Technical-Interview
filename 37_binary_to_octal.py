# Python program to convert binary number to octal 

# method 1 - brute-force and iteration

n=1101101001  #   1551
print(n%1000)
# print(n/1000)
a=n//1000
print(a)
print(n)
print()
print(a%1000)
b=a//1000
print(b)
print(n)
print()
print(b%1000)
c=b//1000
print(c)
print(n)
print()
print(c%1000)
d=c//1000
print(d)
print(n)
print()
print(oct(0b1101101001))
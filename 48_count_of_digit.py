# Python progrsm to count the numebr the digit in a particular number

# method 1 - using len() method
n=int(input("Enter the number :"))
print(len(str(n)))

# method 1 - using modulus operator and brut force
n=int(input("Enter the number :"))
cnt=1
while n>0:
    n=n//10
    cnt=cnt+1
print(cnt)

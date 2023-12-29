# Python progrsm to count the numebr the digit in a particular number

# method 1 - using modulus operator and brut force
try:
    n=int(input("Enter the number :"))
    cnt=0
    while n>0:
        n=n//10
        cnt=cnt+1
    print(cnt)
except:
    print("Enter a valid input.")

# method 2 - using len() method
try:
    n=int(input("Enter the number :"))
    print(len(str(n)))
except:
    print("Enter a valid input.")

# method 3 - using recursion
try:
    n=int(input("Enter the number :"))
    cnt=1
    def digit_count(a):
        if a==0:
            return print(end="")
        global cnt
        cnt+=1
        digit_count(a//10)
    digit_count(n//10)
    print(cnt)
except:
    print("Enter a valid input.")

# Python program to find the occurence of a particular digit in a number.

# Method 1 - using brut-force and iteration
try:
    n=int(input("Enter the number :"))
    m=int(input("Enter the digit :"))
    cnt=0
    while n>0:
        a=n%10
        if a==m:
            cnt+=1
        n=n//10
    print(cnt)
except:
    print("Enter a valid input value.")

# method 2 - using string data-type
try:
    n=input("Enter the number :")
    m=input("Enter the digit :")
    cnt=0
    for i in n:
        if i==m:
            cnt+=1
    print(cnt)
except:
    print("Enter a valid input value.")

# method 3 - using built-in method
try:
    n=input("Enter the number :")
    m=input("Enter the digit :")
    print(n.count(m))
except:
    print("Enter a valid input value.")
    
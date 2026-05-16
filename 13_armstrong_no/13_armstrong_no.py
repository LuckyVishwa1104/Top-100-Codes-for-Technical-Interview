# python program to check wheteher a number is a armstrong nuber or not a armstrong number
# an ARMSTRONG number is a number for which the sum of each digit of number raised to the power of total digit present in number is equal to number itself

# method 1 - by using simple iteration
try:
    n=input("Enter number :")
    sum=0
    l=len(n)
    for i in n:
        sum = sum+int(i)**l
    if n==str(sum):
        print(f'{n} is a Armstrong number.')
    else:
        print(f"{n} is not a Armstrong number")
except:
    print("Enter a valid Integer number.")

# method 2 - using recurssion
try:
    m=input()
    l=len(m)
    def arm(o):
        if o>=l:
            return 0
        a=int(m[o])**l
        sum=a+arm(o+1)
        return sum
    if m==str(arm(0)):
        print(f"{m} is a Armstrong number.")
    else:
        print(f"{m} is not a Armstrong number.")
except:
    print("Enter a valid integer number.")

# emthod 3 - using modulus and floor division operator
try:
    s=int(input())
    n=s
    l=len(str(n))
    sum=0
    while n>0:
        a=(n%10)**l
        sum = sum + a
        n=n//10
    if s == sum:
        print(f"{s} is a Armstrong number.")
    else:
        print(f"{s} is not a Armstrong number.")
except:
    print("Enter a valid number.")

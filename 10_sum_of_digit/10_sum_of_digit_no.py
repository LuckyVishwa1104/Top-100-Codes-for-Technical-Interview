# python program to find sum of digits of a numbers

# method 1 - using type casting
try:
    n=int(input("Enter number :"))
    sum=0
    for i in str(n):
        sum=sum+int(i)
    print(sum)
    pass
except:
    print("Enter valid numeric value")

# method 2 - using modulus operator
try:
    q=int(input("Enter number :"))
    sum=0
    while q>0:
        a=q%10
        sum=sum+a
        q=q//10
    print(sum)
except:
    print("Enter valid numeric value.")

# method 3 - using recurssion
try:
    n=int(input("Enter number :"))
    def sum(n):
        if n<=0:
            return 0
        a=n%10
        summ=a+sum(n//10)
        return summ
    print(sum(n))
except:
    print("Enter valid numeric value.")


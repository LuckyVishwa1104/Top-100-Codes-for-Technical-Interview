# python program to check whether number is a perfect number or not
# perfect number - a number is a perfect number if the sum of its factors is equal to number itself

# method 1 - using iterations
try:
    n=int(input("Enter the number :"))
    sum=0
    for i in range(1,n//2+1):
        if n%i == 0:
                sum = sum+i
    if sum==n:
        print(f'{n} is a perfect number.')
    else:
        print(f'{n} is not a perfect number.')
except:
     print("Enter a valid integer value.")

# method 2 - using recursion
try:
    m=int(input("Enter number :"))
    sum=0
    def perfect_number(n):
        if n==m:
            return print(end="")
        global sum
        if m%n == 0:
            sum=sum+n
        perfect_number(n+1)
    perfect_number(1)
    if sum==m:
        print(f'{m} is a perfect number.')
    else:
        print(f'{m} is not a perfect number.')
except:
    print("Enter a valid integer value")

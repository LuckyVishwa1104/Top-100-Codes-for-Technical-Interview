# python program to find sum of numbers in provided range
# method 1 - traditional way
try:
    m,n=map(int,input().split(','))
    sum=0
    for i in range(m,n+1):
        sum=sum+i
    print(sum)
except:
    print("Enter valid range i.e. from starting to ending n,m")

# method 2 - using recurssion
try:
    m,n=map(int,input().split(','))
    def sum(m,n):
        if m>n:
            return 0
        summ=m+sum(m+1,n)
        return summ
    print(sum(m,n))
except:
    print("Enter valid range i.e. from starting to ending n,m")

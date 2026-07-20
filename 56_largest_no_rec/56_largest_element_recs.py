# Python program to find largest elment of array

# method 1 -using iteration
try:
    n=list(map(int,input("Enter the element of array separated by spaces :").split()))
    maxx=n[0]
    for i in n:
        if i>maxx:
            maxx=i
    print(maxx)
except:
    print("Something went worng!!!")

# method 2 - using recursion
try:
    n=list(map(int,input().split()))
    maxx=n[0]
    def find_max(a):
        if a==len(n):
            return
        global maxx
        if n[a]>maxx:
            maxx=n[a]
        find_max(a+1)
        pass
    find_max(0)
    print(maxx)
except:
    print("Something went worng!!!")

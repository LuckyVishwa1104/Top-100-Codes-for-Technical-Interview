# python program to reverse a number

# method 1 - using slicing operation
try:
    n=input()
    print(n[::-1])
except:
    print("Enter a valid number")

# mehtod 2 - using string cancatenation and for loop
try:
    n=input()
    rs=""
    for i in range(1,len(n)+1):
        rs=rs+n[-i]
    print(rs)
except:
    print("ENter valid number.")

# method 3 - using array and brut force
try:
    num=int(input())
    from array import *
    arr1=array('i',[])
    for i in str(num):
        arr1.append(int(i))
    for i in range(len(arr1)-1,-1,-1):
        print(arr1[i],end="")
    print()
except:
    ("Enter a vlaid number.")

# method 4 -using recursion
try:
    n=input("Enter the number :")
    i=1
    def rev(i):
        if i>len(n):
            return ""
        re=n[-i]
        s=re+rev(i+1)
        return s
    print(rev(i))
except:
    print("Enter a valid number.")

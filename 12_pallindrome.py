# python program to check the pallindrome natuer of string or number

# method 1 - using simple iteration
try:
    n=input()
    re=''
    for i in range(1,len(n)+1):
        re=re+n[-i]
    if n==re:
        print(f'{n} is a pallindrome.')
    else:
        print(f'{n} is not a pallindrome')
except:
    print("Enter valid valuse.")

# method 2 - using slicing operatoin
try:
    n=input("Enter a Number or string :")
    if n==n[::-1]:
        print(f'{n} is a pallindrome')
    else:
        print(f"{n} is not a pallindrome.")
except:
    print("Enter a valid value.")

# method 3 - using recurssion
try:
    n=input()
    i=1
    def palli(i):
        if i>len(n):
            return ""
        a=n[-i]
        re=a+palli(i+1)
        return re
    if palli(i)==n:
        print(f"{n} is a plalindrome.")
    else:
        print(f"{n} is not a Pallindrome.")
except:
    print("Enter a valid value.")

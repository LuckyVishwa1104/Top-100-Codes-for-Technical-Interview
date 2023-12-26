# Python program to check whether a number is sum of two prime nuber or not

# method -1 : brut-force
try:
    n=int(input("Enter the number :"))
    l=[]
    for j in range(2,51):
        for i in range(2,j):
            if j%i==0:
                break
        else:
            l.append(j)
    flag=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
                flag=1
                print(l[i],'+',l[j],'=',l[i]+l[j])
                break
        if flag==1:
            break
except:
    print("Enter teh coerrect integer value.")

# method 2 - using recurssion
try:
    nn=int(input("Enter the number :"))
    l=[]
    def func1(a):
        if a>nn:
            return print(end="")
        def func2(j,a):
            if j>=a:
                l.append(j)
                return print(end="")
            if a%j==0:
                return print(end="")
            func2(j+1,a)
        func2(2,a)
        func1(a+1)
    func1(2)
    flag=False
    def func3(m):
        if flag==True:
            return print(end="")
        if m>=len(l):
            return print(end="")
        def func4(a,mm):
            if a>=len(l):
                return print(end="")
            if l[mm]+l[a]==nn:
                global flag
                flag=True
                return print(l[mm],"+",l[a],"=",nn)
            func4(a+1,mm)
        func4(m+1,m)
        func3(m+1)
    func3(0)
except:
    print("Enter the valid integer value.")

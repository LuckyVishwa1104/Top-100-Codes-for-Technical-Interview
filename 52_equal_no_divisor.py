# Python program to find the number of integer having same nunmber of divisor.

# method 1- brut-force
try:
    n=int(input("Enter the nunber :"))
    m=int(input("Enter the number of divisor :"))
    cnt=0
    for i in range(1,n+1):
        cnt_ind=0
        for j in range(1,i+1):
            if i%j==0:
                cnt_ind+=1
        if cnt_ind==m:
            print(i)
            cnt+=1
    print(cnt)
except:
    print("Something went Wrong!!!")

# method 2 - using recursion
try:
    n=int(input("Enter the nunber :"))
    m=int(input("Enter the number of divisor :"))
    cnt=0
    def func1(a):
        if a>n:
            return
        cnt_ind=0
        def func2(b):
            if b>a:
                return
            if a%b==0:
                nonlocal cnt_ind
                cnt_ind+=1
            func2(b+1)
        func2(1)
        if cnt_ind==m:
            global cnt
            cnt+=1
        func1(a+1)
    func1(1)
    print(cnt)
except:
    print("Something went wrong!!!")

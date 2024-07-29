# python program to find the last non-zero digit form a factorial of a number

# using iteration
try:
    n=int(input("Enter the number :"))
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    j=0
    while fac%10 == 0:
        fac = fac//10
        j=j+1
    print(fac%10)
except:
    print("Enter the valid input!")

# using recursion
try:
    n1 = int(input("Enter the number :"))
    fac1 = 1
    def func1(a):
        if a > n1:
            return
        global fac1
        fac1 = fac1 * a
        func1(a+1)
    func1(1)
    facc = 0
    def func2(p):
        if p%10 == 0:
            p = p // 10
        else:
            return
        global facc
        facc = p
        func2(p)
        pass
    func2(fac1)
    print(facc%10)
except:
    print("Enter the valid input!")

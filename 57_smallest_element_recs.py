# python program to find samllest number of the arrsy

# method 1 - using recursion
try:
    n=int(input("ENter teh umber of element :"))
    l=[]
    for i in range(n):
        l.append(int(input()))
    minn=l[0]
    def samllest(a):
        if a>=n:
            return
        global minn
        if l[a]<minn:
            minn=l[a]
        samllest(a+1)
    samllest(0)
    print(minn)
except:
    print("Something went wrong!!!")


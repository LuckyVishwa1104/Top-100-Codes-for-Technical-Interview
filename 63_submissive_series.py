# python programt to find sum of submissive series.
# submissive series is followed by function : - F(n) = 1 + 2*3 + 4*5*6 + ... + 

# methhod 1 - using simple iteration -
ip=int(input("Enter the number :"))
aa = 1
summ = 0
for a in range(1,ip+1):
    p=1
    m=aa
    aa=aa+a
    for b in range(a):
        p=p*m
        m=m+1
    summ = summ +p
print(summ)

# method 2 - using recurssion
read = int(input("Enter the number :"))
aa = 1
summ = 0
def fun1(a):
    global aa
    p=1
    m=aa
    aa=aa+a
    if a>read:
        return 
    def fun2(b):
        if b>a:
            return
        nonlocal p, m
        p=p*m
        m=m+1
        fun2(b+1)
    fun2(1)
    global summ
    summ=summ+p
    fun1(a+1)
fun1(1)
print(summ)

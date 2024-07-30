# python program to print pascal triangle

import math
def combinaiton(a,b):
    c = math.factorial(a)//(math.factorial(b) * math.factorial(a-b))
    return c

# method 1 - by using factorial built-in function and iterations
n = int(input("Enter the number :"))
l1 = []
for i in range(n+1):
    l2 = []
    for j in range(i+1):
        g = combinaiton(i,j)
        l2.append(g)
    l1.append(l2)
print(l1)

# method 2 - using recursion
m = int(input("Enter the number :"))
l3 = []
def func1(p1):
    if p1 >= m+1:
        return
    l4 = []
    def func2(q1):
        if q1 >= p1+1:
            return
        r1 = combinaiton(p1,q1)
        l4.append(r1)
        func2(q1+1)
    func2(0)
    l3.append(l4)
    func1(p1+1)
    pass
func1(0)
print(l3)
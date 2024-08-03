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
print("Iteration approach :",l1)

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
print("Recursion appraoch :",l3)

# method 3 - using object oriented approach
try:
    class PascalTriangle:
        def __init__(self,num):
            self.num = num
            self.l1 = []
    
        def func1(self,n1):
            fac1 = 1
            def factorial(b):
                nonlocal fac1
                if b ==0 :
                    return
                fac1 = fac1 * b
                factorial(b-1)
                pass

            def fac(a): 
                factorial(a)  
                return fac1
            
            return fac(n1)
    
        def combination(self,a1,b1):
            c = self.func1(a1)//(self.func1(b1)*self.func1(a1-b1))
            return c
    
        def pascalTriangle(self):
            def func1(p1):
                if p1 >= self.num+1:
                    return
                l4 = []
                def func2(q1):
                    if q1 >= p1+1:
                        return
                    r1 = self.combination(p1,q1)
                    l4.append(r1)
                    func2(q1+1)
                func2(0)
                self.l1.append(l4)
                func1(p1+1)
            func1(0)

    number = int(input("Enter the number :"))
    obj1 = PascalTriangle(number)
    obj1.pascalTriangle()
    import sys
    sys.stdout.write("OOP approach :")
    sys.stdout.write(str(obj1.l1))
    sys.stdout.write('\n')
    pass
except:
    print("Enter a valid input value!")

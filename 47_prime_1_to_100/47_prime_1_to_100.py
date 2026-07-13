# Python program to display prime number from 1 to 100

# method 1 - using recursion
def func(a):
    if a>100:
        return print(end="")
    def func1(b,a):
        if b>(a)**(0.5): # b==a | b>a//2 | b>a**0.5
            return print(a,end=" ")
        if a%b==0:
            return print(end="")
        func1(b+1,a)
    func1(2,a)
    func(a+1)
func(2)
print()

# method 2 - using brut force
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")

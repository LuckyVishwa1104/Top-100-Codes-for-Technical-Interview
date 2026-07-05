# Python program to find the sum of two fractional number

# method 1 - using brut force 
a,b=map(int,input("Enter the number in a/b form :").split("/"))
c,d=map(int,input("Enter the number in a/b form :").split("/"))
if b==0 or d==0:
    print("Denominator cant be Zero, enter a valid value!!!")
elif b==d:
    print(f'{a+c}/{b}')
elif a==0 and c!=0:
    print(f"{c}/{d}")
elif c==0 and a!=0:
    print(f"{a}/{b}")
elif a==0 and c==0:
    print(0)
else:
    print(f"{(a*d)+(b*c)}/{b*d}")


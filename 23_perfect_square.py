# python program to check whether the number is a perfect square or not
# a number is a perfect square if its root is an integer value.

# method 1 - checking equality of square
n=int(input("Enter a number :"))
m=int(n**(0.5))
if m**2 == n:
    print(f"{n} is a perfect square")
else:
    print(f"{n} is not a perfect square")

# method 2 - checking equality of root
n=int(input("Enter a number :"))
m=n**(0.5)
l=int(m)
if m == l:
    print(f"{n} perfect square")
else:
    print(f"{n} not a Perfect Square")

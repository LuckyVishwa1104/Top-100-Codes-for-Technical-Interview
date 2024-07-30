def fac(a):
    # global fac1
    fac1 = 1
    def factorial(b):
        if b ==0 :
            return
        nonlocal fac1
        fac1 = fac1 * b
        factorial(b-1)
        pass
    factorial(a)
    return fac1
a = fac(6)
print(a)
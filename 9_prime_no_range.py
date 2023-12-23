# python program to display prime numbers in a range.

# method 1 - using n iteration 
try:
    n=eval(input("Enter number :"))
    for i in range(2,n+1):
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            print(i)
except:
    print("Enter valid integer value.")

#method 2 - reducing iteration to n/2
try:
    n=eval(input("Enter number :"))
    for i in range(2,n):
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            print(i)
except:
    print("Enter valid integer value")

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

# method 3- compairing the number of divisor
# prime number usually have number of divisor equal to two
try:
    n=int(input("Enter the number :"))
    m=2
    for i in range(1,n+1):
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt=cnt+1
        if cnt==2:
            print(i)
except:
    print("Something went wrong!!!")

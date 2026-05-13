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


# method 4 - function based approach

def prime_range(num):
    cnt = num + 1
    prime_list = []
    for i in range(2, cnt): 
        temp = False
        cnt2 = int(i ** 0.5) + 1
        for j in range(2, cnt2):
            if (i % j == 0):
                temp = True
                break
        if(temp == False):
            prime_list.append(i)
    return prime_list

try:
    while (True):
        num = int(input("Enter a integer value : "))
        if (num <= 1):
            print("Enter a positive integer value number greate than two")
        else:
            result = prime_range(num)
            print(result)

        choice = input("Do you want to continue the program? (y/n) : ")
        if (choice.lower() == 'n'):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except Exception as e:
    print(f"Exception caught : {e}")


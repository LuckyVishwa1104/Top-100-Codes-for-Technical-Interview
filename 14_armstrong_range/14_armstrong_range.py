# python progfram to display Armstrong numbers in a particular range or sequence

# method 1 - by using simple iteration 
try:
    m=int(input("Enter the number :"))
    for i in range(1,m+1):
        n=str(i)
        sum=0
        l=len(n)
        for j in n:
            sum=sum+(int(j)**l)
        if n==str(sum):
            print(n)
except:
    print("Enter a valid integer number.")

# method 2 - within particular range
a=int(input("Enter starting number :"))
b=int(input("Enter ending number :"))
try:
    for i in range(a,b+1):
        n=str(i)
        sum=0
        l=len(n)
        for j in n:
            sum=sum+(int(j)**l)
        if n==str(sum):
            print(n)
except:
    print("Enter a valid integer number.")

# method 4 - using function based approach

def is_armsrong(num):
    num_len = 0
    while (num // 10 > 0):
        num_len += 1
    
    pow = (1/num_len)
    while (num > 0):
        sum_of_digit = sum_of_digit + (num % 10)*(pow)
        num = num // 10
    
    return sum_of_digit

try:
    while (True):

        num = int(input("Enter positive integer number : "))

        if(num < 0):
            print("Enter positive integer value")

        else:
            for i in range(1, num + 1):
                result = is_armsrong(num)
                if (num == result):
                    print(num, endline="")

        choice = input("Do you want to continue the program? (y/n) : ")
        if (choice.lower() == 'n'):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except Exception as e:
    print(f"Exception caught : {e}")



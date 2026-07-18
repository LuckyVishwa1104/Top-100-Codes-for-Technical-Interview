# Python program to find the number of integer having same nunmber of divisor.

# method 1- brut-force
try:
    n=int(input("Enter the nunber :"))
    m=int(input("Enter the number of divisor :"))
    cnt=0
    for i in range(1,n+1):
        cnt_ind=0
        for j in range(1,i+1):
            if i%j==0:
                cnt_ind+=1
        if cnt_ind==m:
            print(i)
            cnt+=1
    print(cnt)
except:
    print("Something went Wrong!!!")

# method 2 - using recursion
try:
    n=int(input("Enter the nunber :"))
    m=int(input("Enter the number of divisor :"))
    cnt=0
    def func1(a):
        if a>n: 
            return
        cnt_ind=0
        def func2(b):
            if b>a:
                return
            if a%b==0:
                nonlocal cnt_ind
                cnt_ind+=1
            func2(b+1)
        func2(1)
        if cnt_ind==m:
            global cnt
            cnt+=1
        func1(a+1)
    func1(1)
    print(cnt)
except:
    print("Something went wrong!!!")

# method 3 - using module based approach

def equal_divisor(num, divi):
    if (divi == 1):
        return 1
    count = 0
    for i in range(2, num + 1):
        equal_count = True
        count_factor = 0
        for j in range(1, i + 1):
            if (i % j == 0):
                count_factor += 1
                if (divi < count_factor):
                    equal_count = False
                    break
        if (equal_count):
            count += 1
    return count

try:
    while (True):
        
        number = int(input("Enter number : "))
        divisor = int(input("Enter divisor : "))

        if(divisor <= 0 or number <= 0):
            print("Enter positive value")
        else:
            result = equal_divisor(number, divisor)
            print(f"{result} numbers have {divisor} divisors.")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice.lower() == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")



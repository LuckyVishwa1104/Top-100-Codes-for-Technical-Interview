# program to print sum of first n natural number

# method 1 - using for loop
try:
    num=int(input())
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    print(f"Sum of first {num} numbers is {sum}")
except:
    print("Enter valid number.")

# method 2 - using recurssion
try:
    num=int(input())
    def summ(num):
        if num==0:
            return 0
        else:
            sum=num+summ(num-1)
        return sum
    print(summ(num))
except:
    print("Enter a valid Number")

# method 3: function based approach

def sum_n_numbers(num):
    return ((num * (num + 1)) // 2)

try:
    num = int(input('ENTER A VALID INTEGER VALUE : '))

    if (num < 0):
        print("Enter a positive Integer value.")
    else:
        result = sum_n_numbers(num)
        print(f"Sum of first {num} numbers : {result}")

except ValueError as e:
    print("Enter a valid Integer value.")
    print(f"Exception caught : {e}")

except Exception as e:
    print("Some unexpected error occurred.")
    print(f"Exception caught : {e}")


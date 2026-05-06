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

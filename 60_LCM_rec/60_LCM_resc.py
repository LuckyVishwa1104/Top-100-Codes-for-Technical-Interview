# Python program to find the LCM of a given numbers

# code to increase recurison limit
import sys
print(sys.getrecursionlimit())  # to print the current recursion limit
sys.setrecursionlimit(3000)   # to set new recursion limit with specified value
print(sys.getrecursionlimit())

# method 1 - using recursion
n,m=map(int,input().split())
lcm=0
t=False
def func1(a):
    if a>max(n,m):
        return
    def func2(b):
        if b>max(n,m):
            return
        if n*a == m*b:
            global lcm,t
            lcm=n*a
            t=True
            return
        func2(b+1)
    func2(1)
    if t:
        return
    func1(a+1)
func1(1)
print(lcm)

# method 2 - using exception handling

try:
    while(True):
        num1 = int(input("Enter positive integer value : "))
        num2 = int(input("Enter positive integer value : "))

        def hcf(a, b):
            if (b == 0):
                return a
            return hcf(b, a % b)

        hcf1 = hcf(num1, num2)
        lcm = (num1 * num2) // hcf1
        print(f"LCM of {num1} and {num2} => {lcm}")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice.lower() == "n"):
            print("Program finished!")
            break

except ValueError as ve:
    print(f"Invalid input - {ve}")

except ZeroDivisionError as zde:
    print(f"Zero Division Exception - {zde}")

except Exception as e:
    print(f"Exception caught - {e}")

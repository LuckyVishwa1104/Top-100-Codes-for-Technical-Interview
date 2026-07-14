# Python program to display prime number from 1 to 100

# method 1 - using recursion
def func(a):
    if a>100:
        return print(end="")
    def func1(b,a):
        if b>(a)**(0.5): # b==a | b>a//2 | b>a**0.5
            return print(a,end=" ")
        if a%b==0:
            return print(end="")
        func1(b+1,a)
    func1(2,a)
    func(a+1)
func(2)
print()

# method 2 - using brut force
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")

# using module based approach 

def prime_range():
    return [ n for n in range(2,101) if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))]

try:
    while (True):

        result = prime_range()
        print(result)

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


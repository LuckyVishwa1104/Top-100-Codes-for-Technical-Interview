# Python program to find number of ways in which n person can seat on r seats

# method 1 - using permutation formula by recursion
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
try:
    n=int(input("Enter number of persons :"))
    m=int(input("Enter number of seats :"))
    def fac(a):
        if a==0:
            return 1
        facc=a
        return facc*fac(a-1)
    aa=fac(n)
    bb=fac(n-m)
    ways=aa//bb
    print(ways)
except:
    print("Enter valid integer values.")

# method 2 - using iteration
try:
    n=int(input("Enter number of persons :"))
    m=int(input("Enter number of seats :"))
    def fac(a):
        fac=1
        for i in range(1,a+1):
            fac=fac*i
        return fac
    ways=fac(n)//fac(n-m)
    print(ways)
except:
    print("Enter valid values")

# method 3 - using module based approach

# method to find the number of seating arrangement
def seating_combination(person, seat):
    combination = 1
    while (person >= seat):
        combination = combination * person
        person -= 1
    return combination

# driver program 
try:
    while (True):
        num1 = int(input("Enter number of Persons : "))
        num2 = int(input("Enter number of Seats : "))

        if (num1 <= 0 and num2 <= 0):
            print("Enter positive integer values")

        elif (num1 < num2):
            print("Person should be greater than or equal to number of seats")
        
        else:
            result = seating_combination(num1, num2)
            print(f"{result} ways {num1} person can seat on {num2} seats")

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
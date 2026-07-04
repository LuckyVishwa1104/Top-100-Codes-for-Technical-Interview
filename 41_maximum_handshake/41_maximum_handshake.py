# Python program to find maximum number of handshake between n people
# max handshake - person 1 can handshake with other remaining people and repetition of persons is not allowed

# method 1 - using the formula [n*(n-1)]/2
n=int(input("Enter the number :"))
def max_handshake(n):
    ms=(n*(n-1))/2
    print("Maximum shakehand will be",ms)
max_handshake(int(n))

# method 2 - using brut force
n=int(input("Enter the number :"))
sum=0
for i in range(1,n):
    sum=sum+i
print("Maximum shakehand will be",sum)

# method 3 - using module based approach

# lambda function for calculating max handshake
max_handshake = lambda num : (num*(num-1))/2

# driver program 
try:
    while (True):
        num1 = int(input("Enter number of Persons : "))

        if (num1 <= 0):
            print("Enter positive integer values")
        
        else:
            result = max_handshake(num1)
            print(f"{num1} hand shake are possible!")

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


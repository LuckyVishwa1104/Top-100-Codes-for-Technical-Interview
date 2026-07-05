# Python program to find the sum of two fractional number

# method 1 - using brut force 
a,b=map(int,input("Enter the number in a/b form :").split("/"))
c,d=map(int,input("Enter the number in a/b form :").split("/"))
if b==0 or d==0:
    print("Denominator cant be Zero, enter a valid value!!!")
elif b==d:
    print(f'{a+c}/{b}')
elif a==0 and c!=0:
    print(f"{c}/{d}")
elif c==0 and a!=0:
    print(f"{a}/{b}")
elif a==0 and c==0:
    print(0)
else:
    print(f"{(a*d)+(b*c)}/{b*d}")

# method 2 - using module based approach

def euclidean_hfc(num1, num2):
    while num2 > 0:
        temp = num1
        num1 = num2
        num2 = temp % num2
    return num1

def fractional_sum(nume1, deno1, nume2, deno2):
    nume3 = (nume1 * deno2) + (deno1 * nume2)
    deno3 = deno1 * deno2
    hcf = euclidean_hfc(abs(nume3), abs(deno3))
    nume3 = nume3 // hcf
    deno3 = deno3 // hcf
    if deno3 < 0:
        deno3 *= -1
        nume3 *= -1
    return nume3, deno3

try:
    while (True):
        nume1, deno1 = map(int, input("Enter 1st fraction : ").split("/"))
        nume2, deno2 = map(int, input("Enter 2nd fraction : ").split("/"))

        if (deno1 == 0 or deno2 == 0):
            print("Denominator can not be 0!")
        else:
            result = fractional_sum(nume1, deno1, nume2, deno2)
            print(f"{nume1}/{deno1} + {nume2}/{deno2}  ====>  {result[0]}/{result[1]}")

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


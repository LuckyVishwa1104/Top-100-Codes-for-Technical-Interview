# python program to convert binary number into integer or decimal.

# emthod 1 - using brut force and iterations
try:
    n=int(input("Enter the Binary number :"))
    m=str(n)[::-1]
    sum=0
    for i in range(0,len(m)):
        if int(m[i])==1:
            sum=sum+2**(i)
    print(sum)
except:
    print("Enter a valid integer value.")

# method 2 - using bubilt-in funciton
# int(num,2) - this function is used to convert binary input into decimal value
# it accept two parameters first is the number in string data-type and second is the identifier(2 - for binary, 8 - for octal, 16 - for hexa-decimal)

try:
    n=int(input("Enter the binary number :"))
    deci=int(str(n),2)
    print(deci)
except:
    print("Enter a valid integer value.")

# method 3 - using recurssion
try:
    m=int(input("Enter the binary number :"))
    st=str(m)[::-1]
    sum=0
    def bin_to_oct(n):
        if n>=len(st):
            return print(end="")
        if int(st[n]) == 1:
            global sum
            sum=sum+2**(n)
        bin_to_oct(n+1)
    bin_to_oct(0) 
    print(sum)   
except:
    print("Enter a valid integer value.")

# method 4 - using module based appraoch

def binary_to_decimal(bin):
    bin_str = str(bin)
    bin_str_rev = bin_str[::-1]
    digit_sum = 0
    expo = 0
    for i in bin_str_rev:
        pow = int(i) * (2**expo)
        digit_sum = digit_sum + pow
        expo += 1
    return digit_sum

try:
    while(True):

        num = int(input("Enter positive integer value : "))
        if (num <= 0 or len(str(num)) < 4):
            print("Enter value in decimal form")
        else:
            reuslt = binary_to_decimal(num)
            print(reuslt)

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")



# Python program to convert octal number into its equvalent binary number

# method 1 - using brut-force
n=int(input("Enter the octal unmber :"))
octl=""
while n>0:
    a=n%10
    j=0
    srt=""
    while j<3:
        b=a%2
        srt=str(b)+srt
        j=j+1
        a=a//2
    octl=srt+octl
    n=n//10
print(int(octl))

# method 2 - using recursion
import sys
n=int(input("Enter the octal number :"))
bina=""
def octal_to_binary(n):
    if n<=0:
        return print(end="")
    a=n%10
    srt=""
    def binary(a,j):
        if j>=3:
            return print(end="")
        m=a%2
        nonlocal srt
        srt=str(m)+srt
        binary(a//2,j+1)
        pass
    binary(a,0)
    global bina
    bina=srt+bina
    octal_to_binary(n//10)
    pass
octal_to_binary(n)
print(int(bina))

# method 3 - using built-in method
n=input("Enter the octal number :")
bina=bin(int(n,8))
print(bina)

# method 4 - using module based approach

# dictionary for octal to binary mapping
octal_binary_map = {
	0 : "000",
	1 : "001",
	2 : "010",
	3 : "011",
	4 : "100",
	5 : "101",
	6 : "110",
	7 : "111",
}

# method to check valid octal number
def is_valid_octal(octalNum):
    octalNumStr = str(octalNum)
    for i in octalNumStr:
        if i not in "01234567":
            return False
    return True

# method to convert octal to binary 
def octal_to_binary(octal_num):

    if (octal_num == 0):
        return 0;

    binary_num = ""
    while (octal_num > 0):
        remainder = octal_num % 10
        binary_num =  octal_binary_map[remainder] + binary_num
        octal_num = octal_num // 10
    return binary_num.lstrip("0")

# driver program 
try:
    while (True):
        num = int(input("Enter positive integer value : "))

        if (num < 0):
            print("Enter valid decimal number")
        elif (is_valid_octal(num)):
            print("Enter a valid Octal number")
        else:
            result = octal_to_binary(num)
            print(f"Octal {num} = {result} Binary")

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

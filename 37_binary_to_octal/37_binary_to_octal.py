# Python program to convert binary number to octal 

# method 1 - brute-force and iteration

try:
    n=int(input("Enter the binary number :"))
    oct=""
    while n>0:
        a=n%1000
        s=str(a)[::-1]
        sum=0
        for i in range(len(s)):
            if int(s[i]) == 1:
                sum=sum+2**(i)
        oct=oct+str(sum)
        n=n//1000
    print(oct)
except:
    print("Enter a valid integer value!!!")

# method 2 - using built-int methods
try:
    n=int(input("Enter the binary number :"))
    octl=oct(int(str(n),2))
    print(octl)
except:
    print("Enter a valid integer value!!!")

# method 3 - using recursion
try:
    n=int(input("Enter the binary number :"))
    octl=""
    def binary_to_actal(n):
        if n<=0:
            return print(end="")
        a=n%1000
        summ=0
        s=str(a)[::-1]
        def bin_three(i):
            if i>=len(s):
                return print(end="")
            
            if int(s[i])==1:
                nonlocal summ
                summ = summ + 2**(i)
            # print(summ)
            bin_three(i+1)
        bin_three(0)
        # print(summ)
        global octl
        octl=octl+str(summ)
        binary_to_actal(n//1000)
    binary_to_actal(n)
    print(octl)
except:
    print('Some issue occured!!!')

# method 4 - using module based approach

# map for binary and octal linking 
binary_octal_map = {
"0" :	0,
"1" :	1,
"00" :	0,
"01" :	1,
"10" :	2,
"11" :	3,
"000" :	0,
"001" :	1,
"010" :	2,
"011" :	3,
"100" :	4,
"101" :	5,
"110" :	6,
"111" :	7,
}

# method for binary to octal conversion 
def binary_to_octal(binary_num):
    if (binary_num == 0):
        return 0
    
    octal_num = ""
    while (binary_num > 0):
        remainder = binary_num % 1000
        binary_num = binary_num // 1000
        octal_num = octal_num + str(binary_octal_map[str(remainder)])
    return octal_num

# driver program to check the logic
try:
    while (True):
        num = int(input("Enter positive integer value : "))

        if (num < 0):
            print("Enter valid decimal number")
        else:
            result = binary_to_octal(num)
            print(f"Binary {num} = {result} Octal")

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


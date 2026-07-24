# python program to reverse a number

# method 1 - using recursion
try:
    n=int(input("Enter the number :"))
    s=""
    def reverse_nunber(a):
        '''Function to perform a recursoin for reversing a number'''
        if a==0:
            return
        m=a%10
        global s
        s=s+str(m)
        reverse_nunber(a//10)
        pass
    reverse_nunber(n)
    print(int(s))
except:
    print("Something went wrong!!!")

# method 2 - using module based approach and exception 

try:
    while(True):
        number = int(input("Enter number : "))
        rev_num = 0
        def rev_number(num):
            if (num <= 0):
                return
            last_digit = num % 10
            global rev_num
            rev_num = (rev_num * 10) + last_digit
            rev_number(num // 10)
        rev_number(number)

        print(f"{number} ===> {rev_num}")

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

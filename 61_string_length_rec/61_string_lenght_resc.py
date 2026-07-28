# python program to find the lenght of string using recurison

# method 1 - using recursion
s=input("Enter the string :")
a=0
def string_lenght(s,d=0):
    if s=="":
        return
    global a
    a+=1
    string_lenght(s[d+1:])
string_lenght(s)
print(a)

# method 2 - using standard recursion and exception
try:
    while(True):
        parent_string = (input("Enter String value : "))

        def str_length(shallow_string, ind):
            if (shallow_string == parent_string):
                return ind
            return str_length(shallow_string+parent_string[ind], ind + 1)

        str_len = str_length("", 0)

        print(str_len)

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


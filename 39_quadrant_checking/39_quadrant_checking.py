# Python program to check in which quadratn the given points lies

# method 1 - using brut-force
def fun(x,y):
    if x==0 and y==0:
        print(f"({x},{y}) lies on origin.")
    elif x>=0 and y>=0:
        if y==0:
            print(f"({x},{y}) lies on positive x-axis.")
        elif x==0:
            print(f"({x},{y}) lies on positive y-axis.")
        else:
            print(f"({x},{y}) lies in first quadrant.")
    elif x<=0 and y<=0:
        if y==0:
            print(f"({x},{y}) lies on negative x-axis")
        elif x==0:
            print(f"({x},{y}) lies on negative y-axis")
        else:
            print(f"({x},{y}) lies in third quadrant.")
    else:
        if x>0 and y<0:
            print(f"({x},{y}) lies in fourth quadrant.")
        else:
            print(f"({x},{y}) lies in second quadrant.")

if __name__=="__main__":
    x=int(input("Enter the first co-ordinate :"))
    y=int(input("Enter the second co-ordinate :"))
    fun(x,y)

# method 2 - using module based appraoch

def check_quadran(x, y):
    if (x == 0 and y == 0):
        return "Origin"
    
    if (x == 0):
        return "Posivite Y-axis" if y > 0 else "Negative Y-axis"
    
    if (y == 0):
        return "Positive X-axis" if x > 0 else "Negative X-axis"
    
    if (x > 0 and y > 0):
        return "First Quadrant"
    
    if (x < 0 and y < 0):
        return "Third Quadrant"
    
    if (x > 0 and y < 0):
        return "Fourth Quadrant"
    
    if (x < 0 and y > 0):
        return "Second Quadrant"
    
    return "Lies somewhere universe"

# driver program 
try:
    while (True):
        num1 = int(input("Enter integer value : "))
        num2 = int(input("Enter integer value : "))

        result = check_quadran(num1, num2)
        print(f"({num1}, {num2}) lies in {result}")

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

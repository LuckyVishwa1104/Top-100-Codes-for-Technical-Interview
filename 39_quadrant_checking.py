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
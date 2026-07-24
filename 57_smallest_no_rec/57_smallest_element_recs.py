# python program to find samllest number of the arrsy

# method 1 - using recursion
try:
    n=int(input("ENter teh umber of element :"))
    l=[]
    for i in range(n):
        l.append(int(input()))
    minn=l[0]
    def samllest(a):
        if a>=n:
            return
        global minn
        if l[a]<minn:
            minn=l[a]
        samllest(a+1)
    samllest(0)
    print(minn)
except:
    print("Something went wrong!!!")

# method 2 - using exception and recursion

try:
    print("Enter space separated element of array")
    arr = list(map(int, input().split()))

    smallest = arr[0]
    def smallest_element(num):
        if (num == (len(arr) - 1)):
                    return
        global smallest
        if (arr[num] < smallest):
            smallest = num
        
        smallest_element(num + 1)
    smallest_element(0)

    print(f"Laregest element of {arr} = {smallest}")

except ValueError as ve:
    print(f"Invalid input - {ve}")

except ZeroDivisionError as zde:
    print(f"Zero Division Exception - {zde}")

except Exception as e:
    print(f"Exception caught - {e}")



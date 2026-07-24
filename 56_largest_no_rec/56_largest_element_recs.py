# Python program to find largest elment of array

# method 1 -using iteration
try:
    n=list(map(int,input("Enter the element of array separated by spaces :").split()))
    maxx=n[0]
    for i in n:
        if i>maxx:
            maxx=i
    print(maxx)
except:
    print("Something went worng!!!")

# method 2 - using recursion
try:
    n=list(map(int,input().split()))
    maxx=n[0]
    def find_max(a):
        if a==len(n):
            return
        global maxx
        if n[a]>maxx:
            maxx=n[a]
        find_max(a+1)
        pass
    find_max(0)
    print(maxx)
except:
    print("Something went worng!!!")

# method 3 - using recurssion and module based approach
try:
    print("Enter space separated element of array")
    arr = list(map(int, input().split()))

    largest = arr[0]
    def largerst_element(num):
        if (num == (len(arr) - 1)):
                    return
        global largest
        if (arr[num] > largest):
            largest = num
        
        largerst_element(num + 1)
    largerst_element(0)

    print(f"Laregest element of {arr} = {largest}")

except ValueError as ve:
    print(f"Invalid input - {ve}")

except ZeroDivisionError as zde:
    print(f"Zero Division Exception - {zde}")

except Exception as e:
    print(f"Exception caught - {e}")


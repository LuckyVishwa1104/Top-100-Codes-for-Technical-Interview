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


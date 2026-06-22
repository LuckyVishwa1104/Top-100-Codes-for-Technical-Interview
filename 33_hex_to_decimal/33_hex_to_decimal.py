# Python program to convert Hexadecimal into decimal

# method 1 - using brut-force, list and iteration
try:
    n=input("Enter the Hexadecimal nunber :")
    list1=list(str(n)[::-1])
    if "A" in list1:
        list1[list1.index("A")]=10
    if "B" in list1:
        list1[list1.index("B")]=11
    if "C" in list1:
        list1[list1.index("C")]=12
    if "D" in list1:
        list1[list1.index("D")]=13
    if "E" in list1:
        list1[list1.index("E")]=14
    if "F" in list1:
        list1[list1.index("F")]=15
    sum=0
    for i in range(len(n)):
        a=int(list1[i])*(16**(i))
        sum=sum+a
    print(sum)
except:
    print("Enter a valid Numeric value.")

# method 2 - using ASCII value
try:
    m=input("Enter the number :")
    n=m[::-1]
    sum=0
    for i in range(len(n)):
        if "0"<=n[i]<="9":
            a=int(n[i])*(16**(i))
            sum=sum+a
        elif "A"<=n[i]<="F":
            a=(ord(n[i])-55)*(16**(i))
            sum=sum+a
    print(sum)
except:
    print("Enter a valid numeric value.")

# method 3 -using recursion function
try:
    m=input("Enter the number :")
    n=m[::-1]
    sum=0
    def hex_to_deci(i):
        if i>=len(m):
            return print(end="")
        global sum
        if "0"<=n[i]<="9":
            a=int(n[i])*16**(i)
            sum=sum+a
        if "A"<=n[i]<="F":
            a=(ord(n[i])-55)*16**(i)
            sum=sum+a
        hex_to_deci(i+1)
    hex_to_deci(0)
    print(sum)
except:
    print('Enter a valid numeric value')

# method 4 - using built-in function
try:
    n=input("Enter the number :")
    deci=int(n,16)
    print(deci)
except:
    print("Enter a valid numeric value.")

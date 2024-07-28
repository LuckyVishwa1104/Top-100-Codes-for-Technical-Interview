# Python program to diaplay all possible sub string of a string

try:
    str1 = input("Enter the string :")
    l1 = [""]
    for i1 in range(len(str1)):
        l2=[]
        for j1 in range(len(l1)):
            l2.append(l1[j1] + str1[i1] )
        l1.extend(l2)
    print(l1)
except:
    print("Enter valid Input!")

# python program to display the permutation of string using recursion
try:
    str2 = input("Enter the string :")
    l3 = [""]
    def func1(a):
        if a>=len(str2):
            return
        l4=[]
        def func2(b):
            if b>=len(l3):
                return
            l4.append(l3[b]+str2[a])
            func2(b+1)
            pass
        func2(0)
        l3.extend(l4)
        func1(a+1)
        pass
    func1(0)
    print(l3)
except:
    print("Enter a valid input!")
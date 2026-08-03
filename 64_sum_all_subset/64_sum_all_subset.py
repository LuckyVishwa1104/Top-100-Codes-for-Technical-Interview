# python program to display all the possible sub-set of given array

arr = list(map(int,input("Enter the space separated elements :").split(" ")))
l1=[[]]
for i in range(len(arr)):
    l2=[]
    for j in range(len(l1)):
        l2.append([arr[i]] + l1[j])
    l1.extend(l2)
print(l1)

# python program to display the sum all the possible sub-set of array
try:
    arr1 = list(map(int,input("Enter the space separated elements :").split(" ")))
    l11=[[]]
    for i1 in range(len(arr)):
        l22=[]
        for j1 in range(len(l11)):
            l22.append([sum([arr[i1]] + l11[j1])])
        l11.extend(l22)
    print(l11)
    summ = 0
    for i2 in l11:
        if i2 == []:
            continue
        summ = summ + i2[0]
    print(summ)

except:
    print("Enter a vaild value/set of elements")

# using recurssion

try:
    arr2 = list(map(int,input("Enter the space separated elements :").split(" ")))
    lst1 = [[]]
    def func1(a):
        lst2 = []
        if a >= len(arr2):
            return
        def func2(b):
            if b >= len(lst1):
                return
            lst2.append([arr2[a]] + lst1[b])
            func2(b+1)
            pass
        func2(0)
        lst1.extend(lst2)
        func1(a+1)
        pass
    func1(0)
    print(lst1)
    summ = 0
    for i2 in lst1:
        if i2 == []:
            continue
        summ = summ + i2[0]
    print(summ)
except:
    print("Enter a valid input!")
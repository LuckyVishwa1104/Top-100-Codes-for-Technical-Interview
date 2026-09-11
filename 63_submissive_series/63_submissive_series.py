# python programt to find sum of submissive series.
# submissive series is followed by function : - F(n) = 1 + 2*3 + 4*5*6 + ... + 

# methhod 1 - using simple iteration -
# ip=int(input("Enter the number :"))
# aa = 1
# summ = 0
# for a in range(1,ip+1):
#     p=1
#     m=aa
#     aa=aa+a
#     for b in range(a):
#         p=p*m
#         m=m+1
#     summ = summ +p
# print(summ)

# # method 2 - using recurssion
# read = int(input("Enter the number :"))
# aa = 1
# summ = 0
# def fun1(a):
#     global aa
#     p=1
#     m=aa
#     aa=aa+a
#     if a>read:
#         return 
#     def fun2(b):
#         if b>a:
#             return
#         nonlocal p, m
#         p=p*m
#         m=m+1
#         fun2(b+1)
#     fun2(1)
#     global summ
#     summ=summ+p
#     fun1(a+1)
# fun1(1)
# print(summ)

def sub_series(num):
    s = 0
    i = 1
    e = 1
    while i <= num:
        p = 1
        for j in range(i):
            p = p * e
            e = e + 1
        s = s + p
        i+=1
    return s

try:
    while(True):
        ip = int(input("Enter value : "))
        result = sub_series(ip)
        print(result)

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

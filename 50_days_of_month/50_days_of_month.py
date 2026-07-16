# Python program to find number of days in a particular month od particular year

# method 1 -using brut-force
m=int(input("Enter month :"))
y=int(input("Enter year :"))
if m==2 and ((y%4==0 or y%100==0) and y%400==0):
    print("NUmber of days is 29")
elif (m==2):
    print("NUmber of days is 28")
elif m in [1,3,5,7,8,10,12]:
    print("NUmber of days is 31")
else:
    print(print("NUmber of days is 30"))


# Python program to convert numbers to words

# method 1 - using brut-force and general logic
num=input("Enter the nunber :")
dict_ref={"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine",
          "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen",
          "10":"ten","20":"twenty", "30":"thirty", "40":"forty", "50":"fifty", "60":"sixty", "70":"seventy", "80":"eighty", "90":"ninety",
          "01":"one", "02":"two", "03":"three", "04":"four", "05":"five", "06":"six", "07":"seven", "08":"eight", "09":"nine","00":""}
# places=["thausand", "hundred", "", ""]
if num[-1]=="0" or num[-2]=="0" or num[-2]=="1":
    l=[num[0],num[1],num[2]+num[3]]
    places=["thausand", "hundred", ""]
else:
    l=list((num[0],num[1],num[2]+"0",num[3]))
    places=["thausand", "hundred and", "", ""]
res=""
for i,j in zip(places,l):
    if j=="0":
        continue
    res=res+dict_ref[j]+" "+i+" "
print(res)

# method 2 - usin gbuilt-in library
from num2words import num2words
n=int(input("Enter the umber :"))
print(num2words(n))


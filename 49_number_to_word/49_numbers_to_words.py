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
from num2words import num2words # type: ignore
n=int(input("Enter the umber :"))
print(num2words(n))

# nethod 3 - using module based approach

def convert_two_digit(num):

    # dictionaries for digit places
    ones = {
        0: "",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    teens = {
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen"
    }

    tens ={
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety"
    }

    if (num < 10):
        return ones[num]
    
    elif(num < 20):
        return teens[num]
    
    else:
        ten = num // 10
        one = num % 10

        if (0 == one):
            return tens[ten]
        
        return tens[ten]+ " " +ones[one]

def convert_three_digit(num):
    if (num < 100):
        return convert_two_digit(num)
    
    hundred = num // 100
    remainder = num % 100

    result = ""

    result += convert_two_digit(hundred) + " Hundred"

    if (0 != remainder):
        result += " " + convert_two_digit(remainder)

    return result

def convert_four_digit(num):

    if (num < 1000):
        return convert_three_digit(num)
    
    thausand = num // 1000
    remainder = num % 1000

    result = ""

    result += convert_three_digit(thausand) + " Thausand"

    if (0 != remainder):
        result += " " + convert_three_digit(remainder)

    return result

def conver_six_digit(num):

    if (0 == num):
        return "Zero"
    
    million = num // 1000000
    remainder = num % 1000000

    result = ""
    result += convert_four_digit(million) + " Million"

    if (0 != remainder):
        result += " " + convert_four_digit(remainder)

    return result

def digit_to_words(num):
    return conver_six_digit(num)

try:
    while (True):
        
        num = int(input("Enter number : "))

        if(num < 0):
            print("Enter positive Integer Value")

        else:

            result = digit_to_words(num)
            print(f"{num}  ===>  {result}")

        choice = input("Do you want to continue the program (y/n) : ")
        if(choice.lower() == "n"):
            print("Program finished!")
            break

except ValueError as e:
    print(f"Invalid Input : {e}")

except ZeroDivisionError as e:
    print(f"Zero division exception : {e}")

except Exception as e:
    print(f"Exception caught : {e}")




# method1
try: 
    num=int(input())
    if num>0:
        print(f"{num} is a positive number.")
    elif num<0:
        print(f"{num} is a negative number.")
    else :
        print(f"{num} is a Zero.")

    # method 2
    print("Positive" if num>0 else "Negative" if num!=0 else "Zero")

except:
    print("Enter a Valid Number.")


# function to check whether number is positive or negative
def sign(no):
    try:
        num = int(no)
        if num > 0:
            print(f'{num} is positive')
        elif num < 0:
            print(f'{num} is negative')
        else:
            print(f'{num} is zero')
    except:
        print('Enter a valid value')

n = int(input('Enter a numeric value: '))
sign(n)


# python program to reverse a number

# method 1 - using recursion
try:
    n=int(input("Enter the number :"))
    s=""
    def reverse_nunber(a):
        '''Function to perform a recursoin for reversing a number'''
        if a==0:
            return
        m=a%10
        global s
        s=s+str(m)
        reverse_nunber(a//10)
        pass
    reverse_nunber(n)
    print(int(s))
except:
    print("Something went wrong!!!")
    
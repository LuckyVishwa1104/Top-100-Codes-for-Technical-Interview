# Python program to find maximum number of handshake between n people
# max handshake - person 1 can handshake with other remaining people and repetition of persons is not allowed

# method 1 - using the formula [n*(n-1)]/2
n=int(input("Enter the number :"))
def max_handshake(n):
    ms=(n*(n-1))/2
    print("Maximum shakehand will be",ms)
max_handshake(int(n))

# method 2 - using brut force
n=int(input("Enter the number :"))
sum=0
for i in range(1,n):
    sum=sum+i
print("Maximum shakehand will be",sum)

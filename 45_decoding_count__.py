# Python program to find the count of decoding of a number

# method 1 - brut force
n=int(input()) #12345
s=str(n)
cnt=1
for i in range(len(s)-1):
    if s[i+1]=='0':
        continue
    if s[i]=='1' or s[i]=='2' and s[i+1]<'7':
        cnt+=1
print(cnt)

# method 2 - using recursion
n=int(input("Enter a valid integer value :"))
s=str(n)
cnt=1
def func(a):
    if a>=len(s)-1:
        return print(end="")
    # if s[a+1]=='0':
    #     func(a+1)
    if s[a]=='1' or s[a]=='2' and s[a+1]<'7':
        global cnt
        cnt+=1
    func(a+1)
    pass
func(0)
print(cnt)

# method 3
def cnt_decoding_digits(dig, a):
    cnt = [0] * (a + 1)
    cnt[0], cnt[1] = 1, 1
    if dig.count("00")>=1:
        return "decoding is not possible"
    for k in range(2, a + 1):
        cnt[k] = 0
        cnt[k] = cnt[k - 1]
        if dig[k-1]=='0':
            continue
        if dig[k - 2] == '1' or (dig[k - 2] == '2' and dig[k - 1] < '7'):
            cnt[k] += cnt[k - 2]
    return cnt[a]
dig = input("Enter Number : ")
print(cnt_decoding_digits(dig, len(dig)))

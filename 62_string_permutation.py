# Python program to diaplay all permutation of a string

s="abc"
l=list(s)
ss=list(s)
for i in range(1,len(s)):
    ss.remove('ss[i]')
    for j in ss:
        l[i]=j
        print(''.join(l))

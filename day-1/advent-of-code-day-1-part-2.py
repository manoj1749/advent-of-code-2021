import sys
n = sys.stdin.readlines()
s = []
for i in n:
    a = i.replace('\n','')
    s.append(int(a))
c = 0
s1 = []
a = len(s)
for i in range(len(s)-2):
    x = s[i]+s[i+1]+s[i+2]
    s1.append(x)
b = len(s1)
for i in range(b-1):
    if s1[i]<s1[i+1]:
        c+=1
print(c)
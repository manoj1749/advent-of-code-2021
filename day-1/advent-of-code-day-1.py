import sys
n = sys.stdin.readlines()
s = []
for i in n:
    a = i.replace('\n','')
    s.append(int(a))
c = 0
a = len(s)
for i in range(len(s)-1):
    if s[i] < s[i+1]:
        c+=1
print(c)
import sys
n = sys.stdin.readlines()
s = []
for i in n:
    a = i.replace('\n','')
    s.append(a)
x=0
y=0
for i in range(len(s)):
    k = s[i]
    if k[0]=='f':
        x+=int(k[-1])
    elif k[0]=='u':
        y+=int(k[-1])
    elif k[0]=='d':
        y-=int(k[-1])
if y<0:
    print(-(x*y))
elif y>0:
    print(x*y)
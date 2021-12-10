import sys
n = sys.stdin.readlines()
s = []
for i in n:
    a = i.replace('\n','')
    s.append(a)
x=0
y=0
aim = 0
for i in range(len(s)):
    k = s[i]
    if k[0]=='f':
        x+=int(k[-1])
        y+=(int(k[-1]))*aim
    elif k[0]=='u':
        aim-=int(k[-1])
    elif k[0]=='d':
        aim+=int(k[-1])
if y<0:
    print(-(x*y))
elif y>0:
    print(x*y)
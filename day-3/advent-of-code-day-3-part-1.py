import sys
n = sys.stdin.readlines()
s = []
for i in n:
    a = i.replace('\n','')
    s.append(a)
g = ''
e = ''
for i in range(0,len(s[0])):
    o = 0
    z = 0
    for j in s:
        if j[i]=='0':
            z+=1
        else:
            o+=1
    if o>z:
        g+='1'
        e+='0'
    else:
        g+='0'
        e+='1'
g = int(g,2)
e = int(e,2)
print(g*e)
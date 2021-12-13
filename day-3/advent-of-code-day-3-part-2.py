import sys
n = sys.stdin.readlines()
s = []
s1 = []
for i in n:
    a = i.replace('\n','')
    s.append(a)
o2 = ''
co2 = ''
for i in s:
    s1.append(i)
for i in range(0,len(s[0])):
    o = 0
    z = 0
    for j in s:
        if j[i]=='0':
            z+=1
        else:
            o+=1
    if z > o:
        o2  += '0'
        x = []
        for a in s:
            if a[i]=='0':
                x.append(a)
    else:
        o2 += '1'
        x = []
        for a in s:
            if a[i]=='1':
                x.append(a)
    s = []
    for a in x:
        s.append(a)
    if len(s)==1:
        o2 = s[0]
        break
for i in range(0,len(s1[0])):
    o = 0
    z = 0
    for j in s1:
        if j[i]=='0':
            z+=1
        else:
            o+=1
    if z > o:
        co2  += '1'
        x = []
        for a in s1:
            if a[i]=='1':
                x.append(a)
    else:
        co2 += '0'
        x = []
        for a in s1:
            if a[i]=='0':
                x.append(a)
    s1 = []
    for a in x:
        s1.append(a)
    if len(s1)==1:
        co2 = s1[0]
        break
print('')
print(o2)
print(co2)
o2 = int(o2,2)
co2 = int(co2,2)
print('')
print(o2)
print(co2)
print('')
print(co2*o2)
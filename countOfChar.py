str="My name is Maya"
d={}
for i in str:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
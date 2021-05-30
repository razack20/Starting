import collections
l=["a","b","b","c","c"]
b=collections.Counter(l)
print(b)

#***************************************#
b=["a","z","z","n"]
d={}
for i in b:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)        

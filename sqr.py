a=[1,2,3,4]
b=[]
for i in a:
    r=(i**2)
    b.append(r)
print(b)



#**************************type 2************************************#




def func(element):
    return (element*element)
d=list(map(func,[1,2,3,4]))
print(d)

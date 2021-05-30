#reversing of string in different ways

a=""
b="razz"
for char in b:  
    a=char+a
print(a)

#********************************************************#

a="razz"
d=a[::-1]
print(d)

#*************************************************************#    
a="razz"
for i in a:
    i=reversed(a)
    c="".join(i)
    print(c)
    break

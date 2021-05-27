def comp(d1,d2):
	get_intersection=(d1.keys()) & (d2.keys())
	new_dict={key:(d1.get(key),d2.get(key)) for key in get_intersection}
	print(new_dict)
comp(d1={'a':1,'b':2,'c':3,'d':4},d2={'b':20,'c':30,'y':40,'z':5})	


#****************************************************************************************#


d1={'a':1,'b':2,'c':3,'d':4}
d2={'b':20,'c':30,'y':40,'z':5}
new_dict={}
get_intersection=set(d1.keys()).intersection(d2.keys())
for key in get_intersection:
	new_dict[key]=d1.get(key),d2.get(key)
print(new_dict)
            
            
            

            
            
            

b={}
def ext(a):
	for i in a:
		if i.endswith(".rst"):
			b[i]=True
		else:
			b[i]=False
	print(b)
ext(['one.json','two.rst','three.py','four.rst'])



#***********************************************************#

b={}
def ext(a):
	for i in a:
		if ".rst" in i:
			b[i]=True
		else:
			b[i]=False
	print(b)
ext(['one.json','two.rst','three.py','four.rst'])

# #*************************************************************#

# def ext(a):
# 	for i in a:
# 		if i.endswith(".rst"):
# 			print((i,"true"))
# 		else:
# 			print(i,"False")
		
# ext(['one.json','two.rst','three.py','four.rst'])


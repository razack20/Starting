import re
def word(a):
	b=re.search("Hello",a)
	if b:
		print("True")
	else:
		print("False")	
word(a="Hello world")	
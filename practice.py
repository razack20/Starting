# sequences = [10,2,8,7,5,4,3,11,0, 1]
# filtered_result = filter (lambda x: x > 4, sequences) 
# print(set(filtered_result)

#************************************************************************#

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults =filter(myFunc, ages)
#
# for x in adults:
#   print(x)

#*****************************************************************************#

# for row in range(5):
# 	for column in range(5):
# 		print("# ",end="")
# 	print()		
	
	
			
#***************************************************************#	



# import itertools
# n = 10
# def fibonacci_nums(x=0, y=1):
#     yield x
#     while True:
#         yield y
#         x, y = y, x + y
# print("First 10 Fibonacci numbers:")
# result = list(itertools.islice(fibonacci_nums(), n))
# print(result)
# square = lambda x: x * x 
# print("\nAfter squaring said numbers of the list:")
# print(list(map(square, result)))


#***************************************************************#

# a=[1,2,3]
# b=[]
# for i in a:
# 	if (i>b):
# 		b.append(i)
# 		print(b)
	


#**************************************************************#	
# newlist={}
# def ex(a):
# 	for x in a:
# 		if".rst" in x:
# 			newlist[x]=True
# 	print(newlist)
# ex(['one.json','two.rst','three.py','four.rst'])		

#**************************************************************#
# lst = input().split(",")
# lst.sort()
# print(",".join(lst))

def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*1
	return f
x = 5
result=fact(x)

print(result)		
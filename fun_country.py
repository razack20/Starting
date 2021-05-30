import itertools
data_list = [ {'country': 'USA', 'state': 'Colorado', 'name': 'Ariyana'}, {'country': 'USA', 'state': 'Missouri', 'name': 'Michelle'}, 
{'country': 'SA', 'state': 'Pretoria', 'name': 'Elon Musk'},{'country': 'SA', 'state': 'Pretoria', 'name': 'ABD'}, {'country': 'Finland', 'state': 'Helsinky', 
'name': 'Linux Torvalds'},{"country": "India","state": "Bengaluru","name": "Virat"},{"country": "India","state": "Kerala","name": "Mithun"}]
for i in data_list:
	c=(itertools.groupby(i,key="India"))
	print(c)

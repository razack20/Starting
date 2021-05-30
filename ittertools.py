import itertools
d={k:v for k,v in itertools.zip_longest("pythonandjava",range(1,8),fillvalue="not found")}
print(d)


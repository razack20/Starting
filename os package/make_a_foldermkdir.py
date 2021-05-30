import os
directory = "Hello"

parent_dir = "C:/Users/RCZS/Documents/be"

path=os.path.join(parent_dir,directory)
os.mkdir(path)
print("directory '%s' created" %directory)

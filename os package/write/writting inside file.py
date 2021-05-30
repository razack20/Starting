import os
path = "C:/Users/RCZS/Documents/be/os package/write/empty.txt"

fd = os.open(path, os.O_RDWR)

s = "GeeksForGeeks: A Computer science portal for Geeks."

line = str.encode(s)

numBytes = os.write(fd, line)


print("Number of bytes written:", numBytes)
os.close(fd)

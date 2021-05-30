for i in range(10):
     f = open('file' + str(i) + '.txt', 'w')
     f.write('some random text')
     f.close()
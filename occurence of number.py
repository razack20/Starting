def count_occurance(num,div):
    counter = 0
    for data in range(1,num+1):
        if data%div == 0:
            counter+=1
    print(counter)
count_occurance(100,5)    

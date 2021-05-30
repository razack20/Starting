def divisor():
    for a in range(1,16):
        if(a%3==0 and a%15==0):
            print(a,"fizzbuzz")
        elif a%5==0:
            print(a,"fuzz")
        elif a%3==0:
            print(a,"buzz")
        else:
            print(a)
divisor()   

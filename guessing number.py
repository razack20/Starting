#guessing game

import random
      
x = random.randrange(1, 16)

count = 0
while count<7:
    count += 1
    h = int(input("enter the number %d time:" %count))

    if(x==h):
        print("Guessed correctly the number is: %d" %x)
        break
    else:
       print("The given input is wrong try again.")
    
if count >=7:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
         

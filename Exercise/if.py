import random
ran = random.randint(1,500)
print (ran)
guess = int(input("input a number"))
i=int(5)
while(guess != ran):
    if(i==1):
        print("fail")
        break
    else:
        if(guess>ran):
            i=i-1
            print("too big,you have ["+str(i)+"] times left to try")
            guess = int(input("input a number again"))
        else:
            i=i-1
            print("too small,you have ["+str(i)+"] times left to try")
            guess = int(input("input a number again"))
if(i != 1 or guess == ran):
    print("✔✔✔猜对了✔✔✔")
else:
    print("you have no chance")

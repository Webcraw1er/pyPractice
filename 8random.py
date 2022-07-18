import random

ranarr=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
ranstr= ''
i=12
while i>0:
    ran= random.choice(ranarr)
    print(ran)
    ranstr+= ran
    print(ranstr)
    i-=1
i=12
print(ranstr)
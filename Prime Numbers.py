l=int(input("Enter Lower Limit"))
h=int(input("Enter Higher Limit"))
c=0 #It will count number of factors. Prime no have 2 factors only
pn=[]#It will store the prime numbers
for i in range(l,h+1):
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        pn=pn+[i]
    c=0
print(len(pn))

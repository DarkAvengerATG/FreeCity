#Accepts a large number and a small number. Then it tells the greatest range between prime numbers.
l=int(input("Enter lower limit : "))
h=int(input("Enter higher limit :"))
#Accepting values
c=0
pn=[]
asc=[]
for i in range(l,h+1):
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        pn=pn+[i]
    c=0
d=len(pn)
pn=pn+[pn[d-1]]
for i in range(d):
    asc=asc+[pn[i+1]-pn[i]]
asc.sort()
print(asc[-1])

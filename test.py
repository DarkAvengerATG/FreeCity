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
#Code in python that accepts two values and returns the greatest difference between two prime numbers lying between them.
#I tried the upper limit as 10,100,1000,10000 etc and it followed the pattern 2,8,20,36...
#I predicted ans of 100000 to be 72, turned out to be true
#1000000 and 10000000 give 114 and 160 respectively.
#And it comes from a known pattern.

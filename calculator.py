import math
a= input("choose a number")
a=int(a)
b= input("choose another number")
b=int(b)
powered = math.pow(a,b)
sa= str(a)
sb=str(b)
spowered=str(powered)
print (sa +" powered by " +sb +" is " +spowered)
sqr = math.sqrt(powered)
ssqr= str(sqr)
print ("the Square Root of "+ spowered +" is " + ssqr)
while ssqr>100000:
	print(ssqr)
	ssqr=ssqr+1
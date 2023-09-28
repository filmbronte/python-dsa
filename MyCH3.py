import numpy as np     #For mathematics
import pylab as pl    #For graphics


def ConvexHull(P):
    L = sorted(P)
    UL = UpperHull(L)
    LL = LowerHull(L)
    CH= UL[:-1]+LL[:-1] 
    return L, UL, LL,CH

def Isleft(a,b,c):   #test if point   c makes right turn
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])>=0	

def UpperHull(L):
    Lupper = []
    Lupper[0:2] = L[0:2]
    print(Lupper)
    for i in range(2,len(L)):
	     Lupper.append(L[i])  # add L(i) to Lupper list
	     while len(Lupper) > 2 and Isleft(Lupper[len(Lupper)-3],Lupper[len(Lupper)-2],Lupper[len(Lupper)-1]) ==1:  
	         del Lupper[len(Lupper)-2]   #delete the middle of last three points from Lupper
    return Lupper 

def LowerHull(L):
    Llower = []
    Lreverse=L[::-1] #reverse the list
    Llower[0:2] = Lreverse[0:2]
    print(Llower)	
    for i in   range(2,len(Lreverse)):
         Llower.append(Lreverse[i])  # add Lreverse(i) to Llower list
         print(Llower)
         while len(Llower) > 2 and Isleft(Llower[len(Llower)-3],Llower[len(Llower)-2],Llower[len(Llower)-1]) ==1:  
               del Llower[len(Llower)-2]   #delete the middle of last three points from Llower
    return Llower

	
A =[(5,2),(3,4),(4,5),(7,6),(4,5),(-2,-4),(3,6),(-5,-4),(3,2),(6,0),(-3,10),(-3,-5)]
print("\nOriginal List")
print(A)
L,UL,LL,CH = ConvexHull(A)
print("\nSorted List")
print(L)
print("\nUpperHull")
print(UL) 
print("\nLowerHull")
print(LL)
print("\nConvex Hull")
print(CH)
x=[]
y=[]
for i in range(len(CH)):
   x.append(CH[i][0])
   y.append(CH[i][1])
x.append(CH[0][0])
y.append(CH[0][1])  
pl.plot(x,y,'g-')

 
for i in range(len(L)):
    pl.plot(L[i][0],L[i][1],'ro')

pl.show()
pl.close()

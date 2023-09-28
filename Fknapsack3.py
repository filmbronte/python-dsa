M = 20.0  #Capacity
P = [24.0,15.0,25.0] #Profit
W = [15.0,10.0,18.0]  #Weights
 
#The list must have already been sorted in terms of P./W
 

x=[]
for i in range(len(P)):
    x.append(0)             #initialization.
capacity = M

for i in range(len(x)):
 
    if W[i]> capacity:
        break
    else:
       x[i] = 1
       capacity = capacity -W[i]
if i<=len(x)-1:
       x[i] =capacity/W[i]
   

print("\n Fraction solution")
print(x)

str1 = "aabab"
str2 = "babb"

x = list(str1)
y = list(str2)
cost =[[0 for j in range(len(y)+1) ] for i in range(len(x)+1) ] 
cost[0][:]= list(range(len(y)+1))
for i in range(len(x)+1):
   cost[i][0] = i
print(cost)

for i in range(len(x)):
   for j in range(len(y)): 

      if y[j]== x[i]:
          C = 0
      else:
         C = 2
      cost[i+1][j+1] = min (cost[i][j+1]+1,cost[i+1][j]+1,cost[i][j]+C)
      print(("\ncost"), i+1,j+1)
      print(cost[i+1][j+1])
	  
print("\n Cost matrix")
print(cost) 
	  
   
 

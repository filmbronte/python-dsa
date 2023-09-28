Cost = [[0,2,8,6,10**10,10**10],[10**10,0,2,10**10,10**10,10**10],
        [10**10,10**10,0,7,10**10,10**10],[10**10,6,10**10,0,9,3], 
		[10**10,10**10,4,10**10,0,5],[10**10,10**10,4,10**10,10**10,0]] #cost matrix

v = 0  #Starting vertex
S=[]
Dist=[]
for i in range(len(Cost)):
    S.append(0)             #initial no vertices are in set S  of visited vertices.
    Dist.append(Cost[v][i])   # cost if shortest path for edge (v,i)
	
	
S[v] = 1   
Dist[v] = 0 	  #Starting with v, and put it in S

for j in range(1,len(Cost)):  #The jth node to be added to S
    print("\n Minimum Distance to each vertex")
    print(Dist)
    temp=[]      #temporary variable for Dist
    for i in range(len(Cost)):
       if S[i] == 0:
          temp.append(Dist[i])
       else:
          temp.append(10**10)  #filter out vertices in S so that they are not selected
       u = temp.index(min(temp)) #find the index for adding to S
       S[u]=1
       for w in range(len(Cost)):
             if S[w]==0:
  	            Dist[w]= min(Dist[w], Dist[u]+Cost[u][w])

print("\n Minimum Distance to each vertex")
print(Dist)
 	  
	
 

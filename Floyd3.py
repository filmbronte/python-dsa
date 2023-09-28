W=[ [0,10**10,3,10**10],[2,0,10**10,10**10],
    [10**10,7,0,1],[6,10**10,10**10,0]]  #Weighted gragh
D = W
 
for k in range(len(W)):    #  dynamic programming step index k
   
    for i in range(len(W)):
        for j in range(len(W)):
           D[i][j] = min(D[i][j], D[i][k]+D[k][j])
    print(("\n minimum cost at the intermetiate kth step, k="), k+1)
    print(D)

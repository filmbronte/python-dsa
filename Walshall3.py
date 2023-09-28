A=[ [0,1,0,0],[0,0,0,1],
    [0,0,0,0],[1,0,1,0]]  # gragh
R = A
 
for k in range(len(R)):    #  dynamic programming step index k
    for i in range(len(R)):
        for j in range(len(R)):
           R[i][j] =  R[i][j] or (R[i][k] and R[k][j])
    print(("\n Transitive closure at the intermetiate kth step, k="), k+1)
    print(R)

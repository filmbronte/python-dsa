def prim(X):  #Prim's MST algorithm
    T =[]
    Next =[]
    ind = X[0][:].index(min(X[0][:])) #finding the minimum cost edge to vertex 1 (the first edge)
    mincost = X[0][ind]  #initialize mincost
    print(mincost)	
    T.append([1,ind+1])  #adding to the tree
    print(T)
    for i in range(len(X)):  # initialize Next array
       if X[i][0] >X[i][ind]:
          Next.append(ind)
       else:
         Next.append(0) 
  
    Next[0] = -1  #Set Next[0] as -1 as 0 is used in Python
    Next[ind] = -1	
 

    for i in range(1,len(X)-1):   #finding i^th edge
        temp = []    #stores X[j][Next[j]]
 
        for j in range(len(X)):  #Greedy search all vertices
 
           temp.append(X[j][Next[j]]) 
           temp2 = temp
 	   
        for j in range(len(X)):	 
           if Next[j] == -1:
               temp2[j] = 10**20  #change to cost to vertices in the tree a very large number to avoid cycle
        ind = temp2.index(min(temp2)) #finding the minimum cost edge to vertex j
        mincost = mincost + X[ind][Next[ind]] 
        print(mincost)
        T.append([ind+1,Next[ind]+1])  #add edges
        print(T)
        Next[ind] = -1
 
        for k in range(len(X)):
               if Next[k] != -1 and X[k][Next[k]] >X[k][ind]:
                    Next[k] = ind


    return T, mincost

X=[[10**10,2,8,6],[2,10**10,2,6],[8,2,10**10,7],[6,6,7,10**10]]
T, mincost = prim(X)
print("\nPrim's MST")
print(T)
print("\nMinimum cost")
print(mincost)

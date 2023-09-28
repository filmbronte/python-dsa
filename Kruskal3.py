Forest  = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' ] #Set Initial Forest


A = {('a','b'):2, ('a','c'):8,('a','d'):6,  
     ('b','c'):2,('b','d'):6,
     ('c','d'):7,('c','e'):4,('c','f'):4, 
     ('d','e'):9,('d','f'):3,  
     ('f','e'):5}	                       #Edges and their costs

C=[]
for key in list(A.keys()): 
   C.append(  [A[key]] +[key])

print ("\nOriginal graph ")
print(A)
B = sorted(C)
inx = list(range(len(C)))
inx.sort(lambda x,y: cmp(C[x],C[y]))
print ("\nSorted ")
print(B)

print ("\nIndices  of the sorted edges in the orginal list")
print(inx)   # order of the edge
mincost = 0
T =[] 
for i in range(len(inx)):
   edge = C[inx[i]]
 
   u = edge[1][0]
   v = edge[1][1]
 
   for s in range(len(Forest)):
 
       if u in Forest[s]:
        j = s         #Finding the index of u
           
   for s in range(len(Forest)):
       if v in Forest[s]:
        k = s         #Finding the index of v
        
 
   if j != k:   
      Forest.append((Forest[j],Forest[k]))   #Merge  
      del Forest[j]          #Merge
      del Forest[k-1]          #Merge
      T.append((u,v))          #spanning the edge
 
      mincost = mincost + B[i][0]  #calculate mincost
      print ("\n   Added edge and mincost")	  
      print((u,v), mincost)
   else:
      print(("reject "),  (u,v))   
print ("\nFinal MST")	  
print(T)

print ("\nmincost")	
print(mincost)
 

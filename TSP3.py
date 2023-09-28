c=[ [0,8,6,10 ],[4,0,8,7],
    [6,5,0,5],[7,6,4,0]]  #Weighted gragh

g1={}
for i in range(1,len(c)):
   g1.update({i:c[i][0]})   #set S =[]
   print(i,g1)  


g2={} 
for i in range(1,len(c)):
 
   for j in range(1,len(c)):
      if j!=i:
        g2.update({(i,j):c[i][j]+ g1[j]})   #set S = i
        print((i,j), g2)

g3={}
for i in  range(1,len(c)) :
       temp=[]
       for j in  list(set(range(1,len(c))).difference([i])):        #set S = {j,k}
          for k in   list(set(range(1,len(c))).difference([i,j])):  
 
                    temp.append(c[i][j]+g2[(j,k)])
                    print((i,j),temp)
    				 
 
   
      
       g3.update({(i,(j,k)): min(temp)})			
 

 
g={} 
temp=[]
for j in  range(1,len(c)):   #set S={j,k,l}
     #  print j
       for k in   list(set(range(1,len(c))).difference([j])):  
	   #   print k
          for l in list(set(range(1,len(c))).difference([j,k])): 
		    
                  if (j,(l,k)) in g3:
                      temp.append(c[0][j]+g3[(j,(l,k))])
                  else:
                      temp.append(c[0][j]+g3[(j,(k,l))])
                  print(j,(k,l), temp)                				  
g.update({(0,(j,k,l)): min(temp)})		      

print("\ntrace   the costs")
print(g1) 
 	
print("\ntrace   the costs")
print(g2) 
 	

print("\ntrace   the costs")
print(g3) 
 	
print("\ntrace all the costs")
print(g) 
 	
		
 

#graph is in adjacent list representation
graph = {'1':  ['2', '3'],
         '2':  ['1', '4', '5'],
         '3':  ['1', '6','7'] ,
         '4':  ['2','8'],
         '5':  ['2', '8'] ,
         '6':  ['3', '8'] ,
		   '7':  ['3', '8'] , 
			   '8':  ['5', '4','6','7'],  }
		 
def dfs(graph, start,visited =None):
    if visited is None:
       visited = []
    visited.append(start)
	
 

    for vertex in graph[start]:
	       if vertex  not in visited:
	          dfs(graph, vertex, visited)
 
    return visited

visited = dfs(graph, '1')  
print(visited)

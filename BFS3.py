#graph is in adjacent list representation
graph = {'1':  ['2', '3'],
         '2':  ['1', '4', '5'],
         '3':  ['1', '6','7'] ,
         '4':  ['2','8'],
         '5':  ['2', '8'] ,
         '6':  ['3', '8'] ,
		   '7':  ['3', '8'] , 
			   '8':  ['4', '5','6','7'],  }
		 
def bfs(graph, start):
    queue = [start]
    visited = []
 
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited = visited + [vertex] 
            for node in graph[vertex]:
                queue.extend(node)
    return visited

visited=bfs(graph, '1')  
print(visited)
	 

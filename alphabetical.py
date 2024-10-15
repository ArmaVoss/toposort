from collections import deque

def buildGraph(M: list[list[str]], ) -> dict[str, dict[str, int]]:
    graph = {}
    #create a graph using characters as the vertexs
    #L distinct vertexs
    for row in M:
        for col in row:
            if col in graph:
                continue
            else:
                graph[col] = {}
    #creating directed graph
    for i in range(len(M)-1):
        #assume every word same length(35 character)
        for j in range(len(M[0])):
            #check alphabetical order
            if M[i][j] != M[i+1][j]:
                #if char differs, add directed edge between them, starting at the previous word
                graph[M[i][j]][M[i+1][j]] = 1
                break
    print(graph)  
    return graph

def orderAlphabet(G: dict[str, dict[str,int]]) -> str:
    #initialize our visited hashtable
    def dfs(graph, node, visited, stack, pathVisted):
        visited[node] = True
        pathVisited[node] = True
        for neighbor in graph[node].keys():
            if not visited[neighbor]:
                if dfs(graph, neighbor, visited, stack, pathVisited) == True:
                    return True
            elif(pathVisited[neighbor]):
                return True
    
        stack.append(node)
        pathVisited[node] = False
        return False
        
    visited = {}
    pathVisited = {} #used for checking for cycles

    for key in G.keys():
        visited[key] = False
        pathVisited[key] = False

    stack = deque()
    for vertex in G.keys():
        if not visited[vertex]:
            if dfs(G, vertex, visited, stack, pathVisited) == True:
                return "no alphabetical order"

    order = ""
    while stack:
        order += stack.pop()
    return order

M = [
    ['$','%','%','*'],
    ['&', '&', '#', '&'],
    ['&', '&', '#', '@']
]

M2 = [
    ['$', '%', '%', '∗'],
    ['&', '&', '#', '&'],
    ['&', '&', '#', '$']
]

graph = buildGraph(M)
graphTwo = buildGraph(M2)
print(orderAlphabet(graph))
print(orderAlphabet(graphTwo))
n, m = map( int, input().split(" ") )

graph = [ [] for _ in range( n + 1 ) ]

for x in range(m):
    edge = list(map( int, input().split(" ") ))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


pair_edges = [ [False] * ( n + 1 ) for _ in range( n+1 ) ]

def bfs(node, visited):
    nodes=0
    edges=0

    buffer=[ [ 0, node] ]
    while buffer:
        orig, dest = buffer.pop(0)
        #print(buffer, "===", orig, dest, "___", edges, pair_edges[orig][dest])
        if visited[dest] == False:
            #print(dest, "++")
            nodes+=1
            edges+=1
            for child in graph[dest]:
                if child != orig:
                    if pair_edges[dest][child] == False:
                        buffer.append([dest, child])
                        #pair_edges[child][dest]=True
                        #pair_edges[dest][child]=True
                        #edges+=1
            visited[dest]=True

        elif pair_edges[orig][dest] == False:
            pair_edges[orig][dest]=True
            pair_edges[dest][orig]=True
            edges+=1

    return nodes, edges

new_frienships=0
visited = [ False for _ in range( n + 1 ) ]

i=1
while i < len(visited):
    if visited[i] == False:
        nodes, edges = bfs(i, visited)
        new_frienships+=nodes*(nodes-1)/2-edges+1
    i+=1

print(int(new_frienships))

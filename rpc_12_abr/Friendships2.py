n, m = map( int, input().split(" ") )

graph = [ [] for _ in range( n + 1 ) ]

for x in range(m):
    edge = list(map( int, input().split(" ") ))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


pair_edges = [ [False] * ( n + 1 ) for _ in range( n+1 ) ]

def dfs(node, visited, prev):
    if visited[node] == True:
        x=0
        if not pair_edges[prev][node]:
            x=1
            pair_edges[prev][node]=True
            pair_edges[node][prev]=True

        return 0, x

    visited[node]=True
    pair_edges[prev][node]=True
    pair_edges[node][prev]=True

    n=1
    e=1
    for child in graph[node]:
        if child != prev:
            n_r, e_r = dfs(child, visited, node)
            n+=n_r
            e+=e_r

    return n, e

visited = [ False for _ in range( n + 1 ) ]

new_frienships = 0
i=1

while i < len(visited):
    nodes, edges = dfs(i, visited, 0)
    new_frienships+=nodes*(nodes-1)/2-edges+1
    i+=1

print(int(new_frienships))

t = int( input() )

edges = list(map(int, input().split(" ") ))
visited = [False]*t

count = 0
nxt=1

while visited[nxt-1] == False:
    visited[nxt-1] = True
    count+=1
    nxt=edges[nxt-1]


print(count)

#Leetcode 1761
#from pprint import pprint
def minTrioDegree(n, edges):
    adjacency=[ [0]*(n+1) for _ in range(n+1) ]
    sums=[0]*(n+1)
    for edge in edges:
        x, y = edge
        adjacency[x][y] = 1
        adjacency[y][x] = 1
        sums[x]+=1
        sums[y]+=1

    least_deg = float("inf")

    for i in range(n+1):
        for j in range(i, n+1):
            if adjacency[i][j] == 1:
                for k in range(j, n+1):
                    if adjacency[j][k] == 1 and adjacency[k][i] == 1:
                        least_deg=min(least_deg, sums[i]+sums[j]+sums[k]-6)
    return least_deg if least_deg != float("inf") else -1

print(minTrioDegree(6, [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]))
print(minTrioDegree(7, [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]))


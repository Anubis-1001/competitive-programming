def countCompleteComponents(n, edges):
    is_part_cc = [0]*n
    adjacency=[ [i] for i in range(n) ]

    for e in edges:
        adjacency[e[0]].append(e[1])
        adjacency[e[1]].append(e[0])
    for i in range(n): adjacency[i] = sorted(adjacency[i])

    count=0
    for i in range(n):
        if is_part_cc[i]==1: continue
        if isCompleteComponent(i, adjacency): count+=1

        is_part_cc[i]=1
        for nd in adjacency[i]: is_part_cc[nd]=1

    return count

def isCompleteComponent(i, adjacency):
    nodes=adjacency[i]
    for a in adjacency[i]:
        if nodes != adjacency[a]:
            return False

    return True 


print(countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))
print(countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))

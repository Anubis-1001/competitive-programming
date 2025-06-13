def findOrder(numCourses, prerequisites):
    num_prereq=[0]*numCourses
    for p in prerequisites:
        num_prereq[p[0]]+=1

    queue=[i for i in range(0, numCourses) if num_prereq[i] == 0]
    result=[]
    while queue:
        current=queue.pop(0)
        for i in range(0, len(prerequisites)):
            if prerequisites[i][1] == current:
                num_prereq[ prerequisites[i][0] ]-=1
                if num_prereq[ prerequisites[i][0] ] == 0:
                    queue.append(prerequisites[i][0])
        result.append(current)

    if len(result) == numCourses:
        return result
    return []


print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

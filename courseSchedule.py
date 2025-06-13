def findOrder(numCourses, prerequisites):
    num_prereq=[0]*numCourses
    for p in prerequisites:
        num_prereq[p[0]]+=1

    result=[i for i in range(0, numCourses) if num_prereq[i] == 0]
    l=len(prerequisites)
    i=0
    #print(num_prereq)
    while len(prerequisites) > 0:
        #print(prerequisites)
        if i >= len(prerequisites):
            i=0
            if l == len(prerequisites):
                return [] 
            l=len(prerequisites)
            continue

        n=num_prereq[ prerequisites[i][1] ]
        if n == 0:
            num_prereq[ prerequisites[i][0] ]-=1
            if num_prereq[ prerequisites[i][0] ] == 0:
                result.append(prerequisites[i][0])
            prerequisites.pop(i)
        i+=1

    return result


print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

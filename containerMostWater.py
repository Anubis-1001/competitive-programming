def maxArea(height):
    if len(height) == 2:
        return min(height)

    maxArea = 0
    indexes = [ x for x in range(0, len(height)) ]
    indexes.sort(key=lambda x: height[x])
    traversed = [False]*len(height)
    tail=0
    head=len(height)-1

    for i in indexes:
        traversed[i] = True
        while traversed[tail]: 
            if tail >= len(height)-1:
                return maxArea
            tail+=1
        while traversed[head]:
            if head <= 0:
                return maxArea
            head-=1
        maxArea=max(maxArea, abs(tail-i)*height[i], abs(head-i)*height[i])
        print(maxArea, i, head, tail, traversed)

    return maxArea

#print(maxArea([1,8,6,2,5,4,8,3,7]))
#print(maxArea([1,1]))
#print(maxArea([1,2]))
print(maxArea([1,2,4,3]))


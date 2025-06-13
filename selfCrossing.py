def isSelfCrossing(distance):
    if len(distance) < 4:
        return False

    #points=[[0, 0], [0,distance[0]], [-distance[1], distance[0]],
     #       [-distance[1],distance[0]-distance[2]], [-distance[1]+distance[3], distance[0]-distance[2]]]
    points=[[0,0]]

    #if points[4][1] >= 0 and points[4][0] >= 0:
     #   return True

    for x in range(0, len(distance)):
        #print(points)
        l=len(points)-1
        last=[points[l][0], points[l][1]]
        if x%4==0:
            last[1]+=distance[x]
        elif x%4==1:
            last[0]-=distance[x]
        elif x%4==2:
            last[1]-=distance[x]
        else:
            last[0]+=distance[x]

        if l > 3:
            if l == 4:
                points.insert(0, points[0])
                l+=1
            corner1=points.pop(0)
            corner2=points[l-1]
            corner3=points[1]
            points.append(last)

            if (last[0]-corner1[0])*(last[0]-corner2[0]) <= 0 and (last[1]-corner1[1])*(last[1]-corner2[1]) <= 0 and corner1[0]!=last[0] and corner1[1]!=last[1]:
                opt=[corner2[0], points[l][1]]
                if corner2[1] == opt[1] or corner2[0] == opt[0]:
                    opt=[points[l][0], corner2[1]]
                return isolate(x+1, [opt, points[l-1], points[l], last], distance)

            elif (last[0]-corner3[0])*(last[0]-corner2[0]) <= 0 and (last[1]-corner3[1])*(last[1]-corner2[1]) <= 0:
                opt=[corner3[0], points[l][1]]
                if last[1] == opt[1] or last[0] == opt[0]:
                    opt=[points[l][0], corner3[1]]
                return isolate(x+1, [corner3, opt, corner2, last], distance)
        else:
            points.append(last)

    return False

def isolate(x, points, distance):
    return points


#print(isSelfCrossing([2,1,1,2]))
#print(isSelfCrossing([1,1,1,2,1]))
print(isSelfCrossing([1,1,2,1,1]))

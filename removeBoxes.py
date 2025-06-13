def removeBoxes(boxes):
    cm=[1]
    for x in range(1, len(boxes)):
        if boxes[x]!=boxes[x-1]:
            cm.append(cm[len(cm)-1]+1)
        else:
            l=len(cm)
            cm[l-1]+=1

    matrix = [[0] * len(cm) for _ in range(len(cm))]
    matrix[0][0]=cm[0]**2

    for i in range(1, len(matrix)):

        for j in range(i, -1, -1):
            if i==j:
                matrix[i][j]=(cm[i]-cm[i-1])**2
            else:
                if i==0:
                    local_max=(cm[i])**2+matrix[i-1][j]
                else:
                    local_max=(cm[i]-cm[i-1])**2+matrix[i-1][j]
                    for c in range(i-1, j-1, -1):
                        if boxes[cm[i]-1] == boxes[c]:
                            local_max=max(local_max, 
                                    matrix[i-1][c+1]+
                                    ()**2+
                                    matrix[c-1][i]
                                    )
                matrix[i][j]=local_max

    for x in matrix:
        print(x)

removeBoxes([1,3,2,2,2,3,4,3,1])

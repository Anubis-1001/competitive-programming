import pprint

def calculateMinimumHP(dungeon):

    n_rows = len(dungeon)
    n_columns = len(dungeon[0])
    dp = [ [ [0, 0] for _ in range(n_columns) ] 
            for _ in range(n_rows)
         ]

    for i in range(0, n_rows):
        for j in range(0, n_columns):
            if i == j == 0:
                if dungeon[0][0] < 0:
                    cell_1 = -dungeon[0][0]+1
                    dp[0][0] = [cell_1, cell_1]
                else:
                    dp[0][0]=[1, 1-dungeon[0][0]]
            else:
                if j == 0:
                    l_sum = dp[i-1][j][1]-dungeon[i][j]
                    dp[i][j] = [max(dp[i-1][j][0], l_sum), l_sum]
                elif i == 0:
                    l_sum = dp[i][j-1][1]-dungeon[i][j]
                    dp[i][j] = [max(dp[i][j-1][0], l_sum), l_sum]
                else:
                    l_min = max(dp[i][j-1][1] - dungeon[i][j], dp[i][j-1][0])
                    l_sum = dp[i][j-1][1] - dungeon[i][j]
                    if max(dp[i-1][j][1] - dungeon[i][j], dp[i-1][j][0]) < l_min:
                        l_min = max(dp[i-1][j][1] - dungeon[i][j], dp[i-1][j][0]) 
                        l_sum = dp[i-1][j][1] - dungeon[i][j]
                    dp[i][j] = [max(l_min, l_sum), l_sum]

    #return dp[-1][-1][0]
    return dp

#print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])) 
#pprint.pprint(calculateMinimumHP([
#[-2, -3, 1, -4],
#[-5,  4, -3, 7],
#[20, -11, 1,  1],
#[-1, -10, 44, -4]
#]
#)) 
#pprint.pprint(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
#pprint.pprint(calculateMinimumHP([[100]]))
#pprint.pprint(calculateMinimumHP([[3,-20,30],[-3,4,0]]))
#pprint.pprint(calculateMinimumHP([[1,-4,5,-99],[2,-2,-2,-1]]))
pprint.pprint(calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))

import pprint

def calculateMinimumHP(dungeon):
    n_rows = len(dungeon)
    n_columns = len(dungeon[0])
    dp = [ [0]*n_columns for _ in range(n_rows) ]

    for i in range(0, n_rows):
        for j in range(0, n_columns):
            if i == j == 0:
                dp[i][j] = dungeon[i][j]
            elif j == 0:
                dp[i][j] = dungeon[i][j] + dp[i-1][j]
            elif i == 0:
                dp[i][j] = dungeon[i][j] + dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + dungeon[i][j]

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
pprint.pprint(calculateMinimumHP([[1,-4,5,-99],[2,-2,-2,-1]]))

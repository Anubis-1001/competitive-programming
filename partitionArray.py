import copy 

def minimumDifference(nums):
    s = sum(nums)
    halve = s/2
    dp = [ [0] ]
    for n in nums:
        buffer = copy.deepcopy(dp)
        buffer.append([])
        for row_i in range(len(dp)):
            print(dp, "+++", row_i)
            for cell in range(len(dp[row_i])):
                if row_i + 1 >= len(dp):
                    buffer[len(buffer)-1].append(dp[row_i][cell]+n)
                else:
                    if dp[row_i][cell]+n not in dp[row_i+1]:
                        #print("+++", dp[row_i][cell]+n)
                        buffer[row_i+1].append(dp[row_i][cell]+n)
        dp = buffer
    
    arr = dp[len(nums)//2]
    print(arr)
    print(halve)
    mindiff = abs(halve - arr[0])
    for x in arr:
        if abs(halve - x ) < mindiff:
            mindiff = abs(halve-x)

    return int(mindiff*2)



#print(minimumDifference([2,-1,0,4,-2,-9]))
#print(minimumDifference([2,-1,0,4,-2,-9]))
print(minimumDifference([0,6,11,17,18,24]))
print(minimumDifference([49192,27939,23539,5942,-287070,68765,-68298,-86849,27329,80128,59917,27773,-37798,-4323,17903,94372]))
print(minimumDifference([14082,95061,88968,96247,-76195,82645,93650,10887,65520,-69033,-66003,13309,80849,70685,-63216,-93240]))

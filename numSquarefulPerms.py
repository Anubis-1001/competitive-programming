#Leetcode 996

def numSquarefulPerms(nums):
    n = len(nums)
    m, squares, i = max(nums), defaultdict(bool), 0

    while i*i <= 2*m:
        squares[i*i]=True
        i+=1

    def dfs(bm, last, c):
        if c == n: return 1
        count=0
        processed=set()
        for x in range(n):
            if ( not bm & 1<<x and squares[last+nums[x]] or bm==0 ) and nums[x] not in processed:
                count+=dfs(bm | 1<<x, nums[x], c+1)
                processed.add(nums[x])

        return count

    perms = dfs(0, 0, 0)

    return perms

print(numSquarefulPerms([1,17,8]))
print(numSquarefulPerms([2,2,2]))
print(numSquarefulPerms([4,11,5, 2]))
print(numSquarefulPerms([2,2,2,2,2,2,2,2,2,2,2]))

#N = int(input())
#nums = list(map(int, input().split(" ")))

def dfs(nums, min_v):
    print(nums)
    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        new_arr = [ q for q in nums]
        item = new_arr[i]
        new_arr.pop(i)
        if i < len(new_arr) and item == new_arr[i]:
            j = [ m for m in new_arr]
            j[i]*=2
            min_v=min(min_v, dfs(j, min_v) )

        min_v=min(min_v, dfs(new_arr, min_v) )
    return min_v

print(dfs([4, 2, 2, 1, 8], float("inf")))

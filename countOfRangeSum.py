import bisect

def countRangeSum(nums, lower, upper):
    n = len(nums)
    cumulative_sum = [0]*n
    for i  in range(n):
        cumulative_sum[i] = cumulative_sum[i-1]+nums[i]

    idx = [ j for j in range(n) ]
    sorted_idx = sorted(idx, key=lambda x: cumulative_sum[x])
    sorted_cs = [ cumulative_sum[ind] for ind in sorted_idx ]
    rng_cnt=0

    print(sorted_cs)
    print(sorted_idx)
    for i, idx in enumerate(sorted_idx):
        val = cumulative_sum[idx]
        if lower <= val <= upper: rng_cnt+=1
        s_val = val-upper
        s_val_idx = bisect.bisect_left(sorted_cs, s_val)
        while s_val_idx < n and sorted_cs[s_val_idx] <= val-lower and sorted_cs[s_val_idx] >= s_val:
            if sorted_idx[s_val_idx] < idx:
                rng_cnt+=1
            s_val_idx+=1



    return rng_cnt


print(countRangeSum([-2,5,-1], -2, 2)) #3
print(countRangeSum([0], 0, 0)) #1
print(countRangeSum([0, 0], 0, 0))

#print(bs_righmost([]))

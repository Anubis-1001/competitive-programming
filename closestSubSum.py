import bisect

def minAbsDifference(nums, goal):
    mid = len(nums)//2
    s1 = set([0])
    s2 = set([0])
    h1 = nums[:mid]
    h2 = nums[mid:]
    for arr, s in [ (h1, s1), (h2, s2)]:
        for e in arr:
            buffer = []
            for s_e in s:
                buffer.append(s_e+e)
            for i in buffer:
                s.add(i)
    s2_sorted = list(sorted(s2))
    min_diff = float('inf')
    for e1 in sorted(s1):
        #print(min_diff)
        idx = bisect.bisect_left(s2_sorted, goal-e1)
        idx = min(len(s2_sorted)-1, idx)
        min_diff = min(min_diff, abs(goal-e1-s2_sorted[idx]))
        if idx < len(s2_sorted) - 1:
            min_diff = min(min_diff, abs(goal-e1-s2_sorted[idx+1]))
        if idx > 0:
            min_diff = min(min_diff, abs(goal-e1-s2_sorted[idx-1]))

    return min_diff




print(minAbsDifference( [5,-7,3,5], 6))
print(minAbsDifference( [3, -1, 5, -4, 33], 6))
print(minAbsDifference( [9152249,8464156,-2493402,8990685,-7257152,-1050240,2243737,-82901,8939692], 26915229))

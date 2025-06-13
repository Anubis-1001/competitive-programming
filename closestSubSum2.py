import bisect

def minAbsDifference(nums, goal):
    s = set([0])
    for e in sorted(nums):
        buffer = []
        for s_e in s:
            buffer.append(s_e+e)
        for i in buffer:
            s.add(i)

    sorted_list = sorted(list(s))
    g = bisect.bisect_left(sorted_list, goal)

    l_min = abs( goal - sorted_list[g]  )
    if g < len(sorted_list) - 1:
        l_min = min(l_min, abs(goal-sorted_list[g+1]) )
    if g > 0:
        l_min = min(l_min, abs(goal-sorted_list[g-1]) )
    return  l_min


#print(minAbsDifference( [5,-7,3,5], 6))
#print(minAbsDifference( [3, -1, 5, -4, 33], 6))
print(minAbsDifference( [9152249,8464156,-2493402,8990685,-7257152,-1050240,2243737,-82901,8939692], 26915229))

from heapq import heappush, heappop

def minimumDeviation(nums):
    numbers = [ x if x%2==0 else 2*x for x in nums]
    m = min(numbers)
    max_h = []
    curr_min = float("inf")

    for x in numbers:
        if x != m or curr_min != float("inf"): heappush(max_h, -x)
        else: curr_min = x

    min_diff = -max_h[0]-curr_min

    while max_h and max_h[0]%2 == 0:
        max_h[0]//=2
        l = len(max_h)
        if -max_h[0] < curr_min:
            temp, curr_min =curr_min, -heappop(max_h)
            heappush(max_h, -temp)
        elif ( l >= 2 and max_h[0] > max_h[1] ) or (l >= 3 and max_h[0] > max_h[2]):
            v = heappop(max_h)
            heappush(max_h, v)

        min_diff = min(min_diff, abs(-max_h[0]-curr_min))

    return min_diff


#print(minimumDeviation([1,2,3,4]))
#print(minimumDeviation([4,1,5,20,3]))
#print(minimumDeviation([2,10,8]))
#print(minimumDeviation([4, 2, 5]))
print(minimumDeviation([10,4,3]))

def shortestSubarray(nums, k):
    sum_f=0
    i_f=0
    sum_b=0
    i_b=0
    min_l=len(nums)
    for x in range(0, len(nums)+1):
        if x < len(nums):
            sum_f+=nums[x]
            i_f+=1
        temp_sum_b=sum_b
        temp_i_b=i_b
        print(sum_b)
        print(sum_f)
        while sum_f >= k and temp_i_b < i_f:
            if min_l == len(nums):
                min_l=i_f
            if min_l > i_f-temp_i_b and sum_f-temp_sum_b>=k:
                print("+++")
                print(temp_sum_b)
                print(sum_f)
                print("=====")
                print(i_f)
                print(temp_i_b)
                print("=====")
                min_l = i_f-temp_i_b
                sum_b=temp_sum_b
                i_b=temp_i_b
            temp_sum_b+=nums[temp_i_b]
            temp_i_b+=1

        if sum_f <= 0:
            sum_b=sum_f
            i_b=i_f

    if min_l == len(nums) and sum_f<k:
        min_l=-1

    return min_l


#print(shortestSubarray([2,-1,2], 3))
#print(shortestSubarray([1], 1))
#print(shortestSubarray([1, 2], 4))
#print(shortestSubarray([84,-37,32,40,95], 165))
#print(shortestSubarray([48,99,37,4,-31], 140))
#print(shortestSubarray([-28,81,-20,28,-29], 89))
print(shortestSubarray([-47,45,92,86,17,-22,77,62,-1,42], 180))

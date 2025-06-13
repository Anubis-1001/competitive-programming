def minimumReplacement(nums):

    minStack = [ ]
    n = len(nums)
    nums.append( 10**9 + 1 )

    for i in range(1, n):
        num = nums[i]
        if num <= nums[i+1] and num < nums[i-1]:
            while len(minStack) > 0: 
                if num < nums[minStack[0]]:
                    minStack.pop()
                else:
                    break
            minStack.append(i)

    moves_count=0
    while len(minStack) > 0:
        j = minStack.pop()
        min_num = nums[j]
        j -= 1
        next_num = nums[j]

        sdfsdfsdf
    print( minStack )

minimumReplacement([1,2,3,4,5])
minimumReplacement([3,9,3])
minimumReplacement([5,6,7])
    #while len(minStack) > 0:

     #   j = minStack.pop()
     #  num = nums[j]
     #   residue = nums[ j - 1 
     #   for 




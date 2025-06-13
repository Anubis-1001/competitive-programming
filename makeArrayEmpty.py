from bisect import bisect_left, bisect_right

def countOperationsToEmptyArray(nums):
    #print(nums)
    indexes=[i for i in range(0, len(nums)) ]
    indexes.sort(key= lambda x: nums[x])
    scanned=[]
    opCount=0
    #print(indexes)
    for idx in range(0, len(indexes)):
        #print(opCount)
        #print(scanned)
        if idx == 0:
            opCount+=indexes[idx]+1
        else:
            if indexes[idx-1] < indexes[idx]:
                opCount+=indexes[idx]-indexes[idx-1]-( bisect_left(scanned, indexes[idx]) - bisect_right(scanned, indexes[idx-1]) )
            elif indexes[idx-1] > indexes[idx]:
                opCount+=indexes[idx]+( len(indexes)-indexes[idx-1]-1)-( bisect_left(scanned, indexes[idx]) + ( len(scanned)-bisect_right(scanned, indexes[idx-1]) ) )+1

        #print(opCount)
        #print("======")
        scanned.insert(bisect_left( scanned, indexes[idx]), indexes[idx] )

    return opCount

print(countOperationsToEmptyArray([3,4,-1]))
print(countOperationsToEmptyArray([1,2,4,3]))
print(countOperationsToEmptyArray([1,2, 3]))

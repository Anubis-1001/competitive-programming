def findMedianSortedArrays(nums1, nums2):
    if len(nums1) == 0:
        nums1=nums2
    elif len(nums2) == 0:
        nums2=nums1
    n1, n2=nums1, nums2
    if len(nums1) > len(nums2):
        n1, n2 = nums2, nums1

    size=(len(n1)+len(n2))//2
    if len(n2) > size and n1[0] >= n2[size]:
        return n2[size]

    number1=getindex(n1, n2,size) 
    number2=getindex(n1, n2, (len(n1)+len(n2)-1)//2)
    return (number1+number2)/2


def getindex(nums1, nums2, t):
    s=0
    e=len(nums1)
    if len(nums2) > t and nums1[0] >= nums2[t]:
        return nums2[t]

    while True:
        m=(s+e)//2
        #print(m)
        if t-m-1<0:
            if nums1[t] <= nums2[0]:
                return nums1[t]
            else:
                e=m
                continue
        elif nums1[m] >= nums2[t-m-1] and ( t-m >= len(nums2) or nums1[m] <= nums2[t-m]):
            #print("nums1")
            return nums1[m]
        elif nums1[m] <= nums2[t-m-1] and ( m+1 >= len(nums1) or nums1[m+1] >= nums2[t-m-1] ):
            #print("nums2")
            return nums2[t-m-1]
        if nums1[m] >= nums2[t-m-1]:
            e=m
        else:
            s=m

#print(getindex([1,2], [1,4], 1))
#print(getindex([1,3], [2,7], 1))
#print(getindex([12], [8], 1))
#print(getindex([1, 2], [-1, 3], 0))
print(getindex([3], [1, 2, 4], 1))

def maxDotProduct(nums1, nums2):
    if edgeCase(nums1, nums2) or edgeCase(nums2, nums1):
        if nums1[0] < 0:
            return max(nums1)*min(nums2)
        else: 
            return max(nums2)*min(nums1)

    return max(maxProduct(nums1, nums2), maxProduct(nums2, nums1))

def maxProduct(nums1, nums2):
    dp = [ [0]*len(nums2) for i in nums1 ]
    my_max=-1000000
    for i in range(0, len(dp)):
        for j in range(0, len(dp[0])):
            if i==0:
                dp[i][j]=max(0, nums1[i]*nums2[j], dp[i][j-1])
            elif j==0:
                dp[i][j]=max(0, nums1[i]*nums2[j])
            else:
                dp[i][j]=max(max(0, nums1[i]*nums2[j])+dp[i-1][j-1], dp[i][j-1])

            my_max=max(my_max, dp[i][j])
    return my_max


def edgeCase(nums1, nums2):
    if all(map(lambda x: x < 0 ,nums1)) and all(map(lambda x: x > 0, nums2)):
        return True

#print(maxDotProduct([2,1,-2,5], [3,0,-5]))
print(maxDotProduct([-7,-9,-1,2,2,5,-7,2,-7,5], [7,2,2,-1,-1,1,-4,7,6]))

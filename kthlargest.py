class Solution(object):
        def kthLargestNumber(self, nums, k):
                max_length = 0

                for x in nums:
                    max_length = max( len(nums), max_length)

                for i in range(0, nums, 1):
                    nums[i] = "0"*( max_length - len(nums[i]) ) + nums[i]

                nums.sort()

                                                                                            print(nums)

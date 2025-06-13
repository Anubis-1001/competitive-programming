def threeSum(nums):
    nums.sort()
    print(nums)
    s=0
    e=len(nums)-1
    result=[]
    flag=False
    while e-s >= 2:
        sum_2=nums[s]+nums[e]
        print("=======")
        print(sum_2)
        print(s, e)
        print("=======")
        for n in range(s+1, e):
            if nums[n]==-sum_2:
                result.append([nums[s], nums[n], nums[e]])
                break

        if flag:
            flag=False
            e+=1
            while nums[s]==-nums[e]:
                s+=1
        while s<=e and sum_2 == nums[s]+nums[e]:
            if sum_2 <0:
                s+=1
            else:
                e-=1
                if sum_2==0:
                    flag=True
                
    return result

#print(threeSum([-1,0,1,2,-1,-4]))
#print(threeSum([0, 0, 0]))
#print(threeSum([-2, 0, 1, 1, 2]))
#print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
#print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))


l = int(input())
nums = input().split(" ")
for i in range(len(nums)):
    nums[i] = float(nums[i])

counts = [0, 0, 0, 0, 0]
suma = sum(nums)
for i in range(len(nums)):

    nums[i] = int( (round(nums[i]*100)%5) )

    counts[nums[i]]+=1
    if nums[i] <= 2:
        suma-=nums[i]/100
        nums[i] = 0

suma-=min(counts[4], counts[3])*0.02
print(f'{round(suma, 2): .2f}')

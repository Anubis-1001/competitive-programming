n = int( input() )
nums = list( map( int, input().split(" " ) ) )
r = 1/n
s = sum(nums)

y_less_x=0

for num in nums:
    if num/s > r:
        y_less_x+=num/s-r

print( y_less_x*100 )

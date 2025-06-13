def largestRectangleArea(heights):
    heights.append(-1)
    count_stack=[0]
    number_stack=[-1]
    my_max=0
    for h in heights:
        count=1
        while number_stack[len(number_stack)-1] > h:
            largest_num=number_stack.pop()
            largest_count=count_stack.pop()
            my_max=max(my_max, (largest_count+count-1)*largest_num)
            count+=largest_count

        if number_stack[len(number_stack)-1] == h:
            largest_num=number_stack.pop()
            largest_count=count_stack.pop()
            count+=largest_count

        number_stack.append(h)
        count_stack.append(count)

    for a,n in zip(count_stack, number_stack):
        my_max=max(my_max, n*a)

    return my_max

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea([2,4]))
print(largestRectangleArea([0]))
print(largestRectangleArea([2,1,4,5,1,3,3]))
print(largestRectangleArea([3,6,5,7,4,8,1,0]))
print(largestRectangleArea([2,3]))

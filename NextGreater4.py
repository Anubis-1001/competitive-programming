
def secondGreaterElement(nums):
    first_stack = []
    second_stack = []
    n = len(nums)
    result = [-1]*n

    for i in range(0, n, 1):
        n1 = len( first_stack )
        n2 = len( second_stack )

        while( n2 > 0 ):
            top = second_stack[ n2 - 1 ]
            if nums[i] > nums[top]:
                result[ top ] = nums[i]
                second_stack.pop( n2 -1 )
                n2 = len( second_stack )
            else:
                break

        while( n1 > 0): 
            top =  first_stack[ n1 -1 ] 
            #print(second_stack, nums[i], "---")
            if nums[i] > nums[top]:
                second_stack.insert( n2, top)
                first_stack.pop( n1 -1 )
                n1 = len( first_stack )
                #print(second_stack, nums[i])
            else:
                break

        first_stack.append(i)

    return result

print( secondGreaterElement([11,13,15,12,0,15,12,11,9]) )
print( secondGreaterElement([1, 2, 4, 3]) )
print( secondGreaterElement([3, 3]) )
print( secondGreaterElement([2,4,0,9,6]) )



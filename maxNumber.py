def maxNumber(nums1, nums2, k):
    return max(maxNumberAux(nums1, nums2, k), maxNumberAux(nums2, nums1, k))

def maxNumberAux(nums1, nums2, k):
    numbers1=[[x,0] for x in nums1]
    numbers2=[[x,1] for x in nums2]
    numbers=numbers1+numbers2
    stack=[]

    for n in range(0, len(numbers)):
        stack.append(numbers[n])
        l=len(stack)-1
        while l > 0 and stack[l] > stack[l-1]:
            if stack[l][1] != stack[l-1][1]:
                aux = stack[l]
                stack[l] = stack[l-1]
                stack[l-1] = aux
            elif stack[l][1] == stack[l-1][1]:
                if len(stack) + len(numbers)-n-1 > k:
                    stack.pop(l-1)
            l-=1
    resultado = stack[0:k]
    s1=[]
    s2=[]
    for r in resultado:
        if r[1] == 0:
            s1.append(r)
        else:
            s2.append(r)

    resultado_final=[]
    while len(s1) + len(s2) > 0:
        if len(s1) == 0 or ( len(s2) > 0 and s2[0][0] > s1[0][0]):
            resultado_final.append(s2[0][0])
            s2.pop(0) 
        elif len(s2) == 0 or ( len(s1) > 0 and s1[0][0] > s2[0][0]):
            resultado_final.append(s1[0][0])
            s1.pop(0)
        else:
            if len(s1) < 2 or ( len(s2) >= 2 and s1[1][0] > s2[1][0] ):
                resultado_final.append(s2[0][0])
                s2.pop(0)
            elif len(s2) < 2 or ( len(s1) >= 2 and s2[1][0] > s1[1][0] ):
                resultado_final.append(s1[0][0])
                s1.pop(0) 

    return resultado_final



#print(maxNumber([3,4,6,5],[9,1,2,5,8,3], 5))
#print(maxNumber([6,7],[6,0,4], 5))
#print(maxNumber([8,9],[3,9], 3))
#print(maxNumber([3,9],[8,9], 3))
#print(maxNumber([7,3,8,0,6,5,7,6,2],[2,5,6,4,4,0], 15))
#print(maxNumber([2,5,6,4,4,0],[7,3,8,0,6,5,7,6,2], 15))
print(maxNumber([1,6,5,4,7,3,9,5,3,7,8,4,1,1,4], [4,3,1,3,5,9],21))
#print(maxNumberAux([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15))


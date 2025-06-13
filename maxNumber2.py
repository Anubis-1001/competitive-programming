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
        print(list(map(lambda x:x[0], s1)))
        print(list(map(lambda x:x[0], s2)))
        print(resultado_final)
        print("======")

        m=0
        while len(s1) > m and len(s2) > m and s1[m][0] == s2[m][0]:
            m+=1
        if len(s1) <= m or ( len(s2) > m  and s2[m][0] > s1[m][0] ):
            resultado_final.append(s2[0][0])
            s2.pop(0) 
        elif len(s2) <= m or ( len(s1) > m  and s1[m][0] > s2[m][0] ):
            resultado_final.append(s1[0][0])
            s1.pop(0) 

    return resultado_final


#print(maxNumber([3,4,6,5],[9,1,2,5,8,3], 5))
#print(maxNumber([6,7],[6,0,4], 5))
#print(maxNumber([8,9],[3,9], 3))
#print(maxNumber([3,9],[8,9], 3))
#print(maxNumber([7,3,8,0,6,5,7,6,2],[2,5,6,4,4,0], 15))
#print(maxNumber([2,5,6,4,4,0],[7,3,8,0,6,5,7,6,2], 15))
#print(maxNumber([1,6,5,4,7,3,9,5,3,7,8,4,1,1,4], [4,3,1,3,5,9],21))
#print(maxNumber([5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3], [7,6,7,1,0,1,0,5,6,0,5,0], 31))
#print(maxNumber([8,0,4,4,1,7,3,6,5,9,3,6,6,0,2,5,1,7,7,7,8,7,1,4,4,5,4,8,7,6,2,2,9,4,7,5,6,2,2,8,4,6,0,4,7,8,9,1,7,0], [6,9,8,1,1,5,7,3,1,3,3,4,9,2,8,0,6,9,3,3,7,8,3,4,2,4,7,4,5,7,7,2,5,6,3,6,7,0,3,5,3,2,8,1,6,6,1,0,8,4], 50))
print(maxNumber([8,0,4,4,1,7,3,6,5,9,3,6,6,0,2,5,1,7,7,7,8,7,1,4,4,5,4,8,7,6,2,2,9,4,7,5,6,2,2,8,4,6,0,4,7,8,9,1,7,0], [6,9,8,1,1,5,7,3,1,3,3,4,9,2,8,0,6,9,3,3,7,8,3,4,2,4,7,4,5,7,7,2,5,6,3,6,7,0,3,5,3,2,8,1,6,6,1,0,8,4], 50))
#print(maxNumberAux([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 16))


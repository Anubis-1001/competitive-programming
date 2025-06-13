def splitArraySameAverage(nums):
    avg=[[0,0]]
    a=sum(nums)/len(nums)
    print(a)
    nums.sort()
    for n in nums:
        i=0
        l_avg=[]
        #print("=======")
        #print(avg)
        print(n)
        while i < len(avg):
            new_n=[avg[i][0]+n, avg[i][1]+1]
            if avrg(new_n) < a:
                l_avg.append(new_n)
            elif avrg(new_n) == a and new_n[1]<len(nums):
                return True
            i+=1

        l_avg.sort(key=lambda x: avrg(x))
        #print(avg)
        #print(l_avg)
        #print(l_avg)
        j=0
        for nn in avg:
            while j<len(l_avg) and avrg(nn) > avrg(l_avg[j]):
                j+=1
            l_avg.insert(j, nn)
            j+=1

        avg=l_avg

    return False


def avrg(d_tuple):
    return d_tuple[0]/(max(1, d_tuple[1]))

#print(splitArraySameAverage([1,2,3,4,5,6,7,8]))
#print(splitArraySameAverage([1,3]))
#print(splitArraySameAverage([1,1]))
#print(splitArraySameAverage([5,6,7,11, 16]))
#print(splitArraySameAverage([0,13,13,7,5,0,10,19,5]))
print(splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))

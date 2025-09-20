#arr=[0]*100
#arr=[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,0,0,0,0,0]
#arr=[0,0,1,1,1,1,2,1,1,1,1,1,1,1,0,0,0]
#arr=[0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0]
arr=[0,0,0,0,0,0,0,0,0,0,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0]
def splatter(arr):
    i=0
    while i < len(arr):
        if arr[i] < 2 or i == 0 or i == len(arr)-1:
            i+=1
        else:
            num=arr[i]
            if i > 0:
                arr[i-1]+=num//2
            if i < len(arr)-1:
                arr[i+1]+=num//2
            arr[i]%=2
            i=0

    return arr


#arr[18]=79
print(splatter(arr))
#arr[18]="+++++"
#print(arr)

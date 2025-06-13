#1, 
#22, 
#122, 
#212, 
#221, 
#333, 
#4444, 
#1333, 3331, 3133, 3313, 55555, 14444, 22333, 122333, 666666, 224444, 155555, 1224444



def getPer(s_arr, i, r_set):
    if i == len(s_arr):
        r_set.add("".join(s_arr))
    else:
        for x in range(0+i, len(s_arr)):
            if s_arr[i] == s_arr[x] and i!=x :
                continue
            s_arr[i], s_arr[x] = s_arr[x], s_arr[i]
            getPer(s_arr, i+1, r_set)
            s_arr[x], s_arr[i] = s_arr[i], s_arr[x]
        

#getPer(["1","2","2", "4", "4", "4", "4"], 0)
#getPer(["1","4", "4", "4", "4"], 0)
my_set=set()
getPer(["1","2","2", "4", "4", "4", "4"], 0, my_set)
print(len(my_set))

from collections import defaultdict 

def tallestBillboard(rods):
    max_height = 0
    sum_dict = defaultdict(int)
    for rod in rods:
        sum_dict_copy = sum_dict.copy()
        for rod_sum in sum_dict_copy.keys():
            sum_dict[ rod_sum + rod ] += 1
            if sum_dict[ rod_sum + rod ] > 1 :
                max_height = max( rod_sum + rod, max_height )

        sum_dict[rod] += 1
        if sum_dict[ rod ] > 1:
            max_height = max( rod, max_height )

    print( sum_dict ) 
    return max_height


tallestBillboard( [1,2,3,4,5,6] )


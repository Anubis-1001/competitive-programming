


def tallestBillboard(rods):
    return tallestBillboardAid( [1,2,3,4,5,6], 0, 0, 0, [])

def tallestBillboardAid(rods, i, s1, s2, lengths):
    print(lengths)
    if s1 == s2:
        lengths.append(s1)
    if s1 == s2:
        lengths.append(s1)
    if i == len( rods ):
        return max(lengths)

    for_s1 = tallestBillboardAid(rods, i+1, s1 + rods[i], s2, lengths.copy())
    for_s2 = tallestBillboardAid(rods, i+1, s1, s2 + rods[i], lengths.copy())
    for_none = tallestBillboardAid(rods, i+1, s1, s2, lengths.copy())
    return max( for_s1, for_s2, for_none)


print( tallestBillboard( [1,2,3,4,5,6] ) )


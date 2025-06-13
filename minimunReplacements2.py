def minimumReplacement(nums):
    n = len(nums)
    nums.append( 10**9 + 1 )
    c_min = 10**9 + 1
    moves_count=0

    for i in range(n-1, -1, -1):
        num = nums[i]
        residue = num % c_min
        if num >= c_min:
            quotient = num // c_min
            moves_count += quotient
            if residue == 0:
                moves_count -= 1
            else:
                c_min = residue + ( c_min - residue ) * quotient // ( quotient + 1 )
                #print( residue, num, c_min, "++" )
        else:
            if num < nums[i-1]:
                c_min = num
        print( moves_count, "--", num, "--", c_min)
    print( moves_count )

#minimumReplacement([1,2,3,4,5])
#minimumReplacement([3,9,3])
#minimumReplacement([5,6,7])
#minimumReplacement([2,10,20,19,1])
#minimumReplacement([12,9,7,6,17,19,21])
minimumReplacement([368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223])

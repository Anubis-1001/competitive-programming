#https://codeforces.com/problemset/problem/978/D

N = int(input())
arr = list(map(int, input().split(" ")))

def almostProgression(N, nums):
    if N==1:
        return 0
    f_sum=sum(nums)
    r_coef=N*(N-1)//2
    i=nums[0]
    result=float("inf")
    for n in range(-N, N+1):
        l_sum=f_sum+n
        for initial in [i-1, i, i+1]:
            D=l_sum-initial*N
            if D%r_coef==0:
                res=validate((initial, l_sum, D//r_coef), nums)
                if res != -1:
                    result=min(res, result)
    return result if result != float("inf") else -1

def validate(formula, nums):
    i, s, r = formula
    count=0
    for p, n in enumerate(nums):
        if abs(i+p*r - n) > 1:
            return -1
        else:
            count+=abs(i+p*r - n)

    return count

print(almostProgression(N, arr))

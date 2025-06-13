def kidsWithCandies(candies, extraCandies):
    least = max(candies) - extraCandies
    result = [False]*len(candies)
    for i in range(len(candies)):
        if candies[i] >= least:
            result[i] = True

    return result

print(kidsWithCandies([2,3,5,1,3], 3))

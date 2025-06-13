def divisorGame(n):
    result=[False]*(n+1)
    result[1]=True
    for i in range(1, len(result)):
        d=1
        while d*d <= i:
            if i%d==0 and not result[n-d]:
                result[n]=True
                break
            d+=1


    return result[len(result)-1]





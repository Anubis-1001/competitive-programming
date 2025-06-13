def canPlaceFlowers(flowerbed, n):
    flowerbed.append(0)
    flowerbed.insert(0, 0)
    i=1
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            if flowerbed[i-1] + flowerbed[i+1] == 0:
                n-=1
                if n == 0: return True
            i+=1
        if flowerbed[i]:
            i+=2

    return False

print(canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))

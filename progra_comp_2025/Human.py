import math

num = int(input())

def pyramid(n):
    result=(-1+(1+8*n)**(0.5))/2
    return math.floor(result)

print(pyramid(num))

points = int(input())
triangle_area=0
init_p = input().split(" ")
init_X = float(init_p[0])
init_Y = float(init_p[1])

length=0

for _ in range(points-1):
    pts = input().split(" ")
    p_X = float(pts[0])
    p_Y = float(pts[1])
    length +=  ( init_X-p_X ) ** 2 + ( init_Y-p_Y) **2 
    if init_X < p_Y:
        triangle_area+=( p_X-init_X )*( init_Y + ( p_Y - init_Y)/2 )
    else:
        triangle_area+=( p_X-init_X )*( init_Y + ( p_Y - init_Y)/2 )

    init_X = p_X 
    init_Y = p_Y
print("t", triangle_area)
print("t", length)
ratio = length
sein=1
ptr=1
for _ in range(116):
    sein+=ptr*ratio
    ptr*=ratio

init_Area = (3**(0.5))/4
print(init_Area+3*triangle_area*(ratio**27) )
print(init_Area+3*triangle_area*sein )
print(init_Area+3*triangle_area/(1-ratio) )

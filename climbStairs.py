

f=0
s=1
for x in range(0, n):
    aux=s
    s=f+s
    f=aux

return s

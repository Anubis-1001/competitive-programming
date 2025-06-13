def validArrangement(pairs):
    h={}
    for p in pairs:
        h[p[0]]=h.get(p[0], [])+[p]

    head=[]
    current=[]
    while len(current) + len(head) < len(pairs):
        print("======")
        print(current)
        print(head)
        if len(current) == 0 or len(h.get(current[-1][1], [])) == 0:
            if len(head) > 0 and len(current) > 0:
                if head[-1][1] == current[0][0]:
                    head=head+current

                elif head[0][0] == current[-1][1]:
                    head=current+head
                else:
                    for x in range(0, len(head)):
                        if head[x][1] == current[-1][0] and head[x+1][0] == current[-1][1]:
                            head=head[:x+1]+current+head[x+1:]
                            break
            else:
                if len(head) == 0:
                    head=current
            for k in h.keys():
                if len(h[k]) > 0:
                    current=[h[k].pop(0)]
                    break
        else:
            l=current[-1][1]
            current=current+[h[l].pop(0)]

    return current+head

#print(validArrangement([[5,1],[4,5],[11,9],[9,4]]))
print(validArrangement([[999,990],[356,511],[192,879],[246,945],[322,602],[776,246],[248,126],[503,284],[126,164],[494,731],[862,382],[731,578],[511,277],[122,731],[578,99],[731,277],[847,538],[246,494],[284,138],[382,899],[811,439],[164,99],[485,307],[618,320],[494,511],[413,248],[945,356],[990,614],[138,18],[164,862],[277,164],[826,737],[277,322],[618,122],[291,639],[288,11],[624,485],[740,452],[614,740],[307,903],[457,412],[538,961],[439,122],[961,999],[639,822],[903,503],[961,776],[138,538],[122,826],[99,138],[949,175],[452,847],[320,624],[879,457],[511,961],[835,692],[18,949],[737,413],[822,999],[11,726],[692,618],[899,835],[726,192],[999,452],[602,811],[452,618],[175,246],[99,291],[412,494]]))

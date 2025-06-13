


def candy2(ratings):
    ratings.insert( 0, float('inf') )
    ratings.append( float('inf') )
    n = len(ratings) 
    candies = 0
    neighbor_candy = 0
    prev_neighbor = 0
    descending_seq = 1
    for i in range( 1, n-1, 1): 

        if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
            neighbor_candy = 1
            candies += neighbor_candy
            if descending_seq > 1:
                print( descending_seq, "----")
                print( prev_neighbor )
                candies += descending_seq*( descending_seq + 1)/2 - 1 
                candies -= min( prev_neighbor, descending_seq )
                descending_seq = 1

        elif ratings[i] > ratings[i-1] and ratings[i] <= ratings[i+1]:
            neighbor_candy += 1
            candies += neighbor_candy

        elif ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]: 
            neighbor_candy += 1
            candies += neighbor_candy
            prev_neighbor = neighbor_candy
            neighbor_candy = 0
            descending_seq = 1 
        elif ratings[i] <= ratings[i-1] and ratings[i] > ratings[i+1]: 
            descending_seq += 1

        print( candies )
 
    return candies


#candy( [1,6,10,8,7,3,2] )




def candy(ratings):
    ratings.insert( 0, float('inf') )
    ratings.append( float('inf') )
    n = len(ratings)
    candies = 0
    neighbor_candy = 0
    prev_neighbor = 0
    descending_seq = 1
    for i in range( 1, n-1, 1):

        if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
            neighbor_candy = 1
            candies += neighbor_candy
            if descending_seq > 1:
                print( prev_neighbor )
                candies += descending_seq*( descending_seq + 1)/2 - 1
                candies -= min( prev_neighbor, descending_seq )
                descending_seq = 1
                prev_neighbor = 0

        elif ratings[i] > ratings[i-1] and ratings[i] <= ratings[i+1]:
            neighbor_candy += 1
            candies += neighbor_candy

        elif ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
            neighbor_candy += 1
            candies += neighbor_candy
            prev_neighbor = neighbor_candy
            neighbor_candy = 0
            descending_seq = 2
        elif ratings[i] <= ratings[i-1] and ratings[i] > ratings[i+1]:
            descending_seq += 1

        print( candies )

    return candies


candy( [1,3,2,2,1] )

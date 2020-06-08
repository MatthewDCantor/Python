
"""
Given a list of N items that each have a value V and weight W, find the maximum
value with a given maximum weight Max

Example

N = 4, Max = 7

Val Wt
(1) 1
(4) 3
(5) 4
(7) 5

max value = 9 with (3+4)

Algorithm
1. create max value matrix, m
2. find largest element of max value matrix and find it's composition of items


explation of matrix -->   https://www.youtube.com/watch?v=8LusJS5-AGo
max value matrix

Val Wt | 0 1 2 3 4 5 6 7 (max weight)
 0  0  | 0 0 0 0 0 0 0 0
(1) 1  | 0 1 1 1 1 1 1 1
(4) 3  | 0 1 1 4 5 5 5 5
(5) 4  | 0 1 1 4 5 6 6 9
(7) 5  | 0 1 1 4 5 7 8 9

entry i,j = maximum value including up to i items for a maximum weight j
          = max(val[i]+ m[i-1][j-w[i]], m[i-1][j])


Example input:
Test cases
N Max
(n lines of)
val wt
'2'
'4 7'
'1 1'
'4 3'
'5 4'
'7 5'
'5 10'
'3 1'
'4 3'
'6 2'
'12 7'
'13 8'


"""
rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))

def knapsack(n,max_w,wt,val):

    # create blank max value matrix to be filled
    m = [[0 for x in range(max_w+1)] for y in range(n+1)]

    #fill max value matrix

    for j in range(1,max_w+1):
        for i in range(1,n+1):
            if wt[i] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(val[i]+ m[i-1][j-wt[i]], m[i-1][j])

    print "max value matrix:"
    for i in range(n+1):
        print m[i]

    #find items for max value -- doesn't account for a case of a tie
    y,x = n,max_w
    items = []


    while m[y][x] != 0:
        if m[y][x] == m[y-1][x]:
            y = y-1
        else:
            items.append((val[y],wt[y]))
            x = x - wt[y]
            y = y - 1



    return m[n][max_w]

"""----------Main-----------"""

test_cases = rri()

for t in range(test_cases):

    n,max_w = rrm()
    val = [0 for x in range(n+1)]
    wt = [0 for x in range(n+1)]

    for i in range(1,n+1):
        val[i],wt[i] = rrm()

    print knapsack(n,max_w,wt,val)

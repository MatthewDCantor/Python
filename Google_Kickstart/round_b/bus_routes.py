"""-----------Problem-----------
Bucket is planning to make a very long journey across the countryside by bus.
Her journey consists of N bus routes, numbered from 1 to N in the order she must
take them. The buses themselves are very fast, but do not run often.
The i-th bus route only runs every Xi days.

More specifically, she can only take the i-th bus on day Xi, 2Xi, 3Xi and so on.
 Since the buses are very fast, she can take multiple buses on the same day.

Bucket must finish her journey by day D, but she would like to start the journey
as late as possible. What is the latest day she could take the first bus,
and still finish her journey by day D?

It is guaranteed that it is possible for Bucket to finish her journey by day D.


-----------Input & Output -------------
'3'
'3 10'
'3 7 2'
'4 100'
'11 10 5 50'
'1 1'
'1'

Case #1: 6
Case #2: 99
Case #3: 1


In Sample Case #1, there are N = 3 bus routes and Bucket must arrive
by day D = 10. She could:
Take the 1st bus on day 6 (X1 = 3),
Take the 2nd bus on day 7 (X2 = 7) and
Take the 3rd bus on day 8 (X3 = 2).


In Sample Case #2, there are N = 4 bus routes and Bucket must arrive
by day D = 100. She could:
Take the 1st bus on day 99 (X1 = 11),
Take the 2nd bus on day 100 (X2 = 10),
Take the 3rd bus on day 100 (X3 = 5) and
Take the 4th bus on day 100 (X4 = 50),


In Sample Case #3, there is N = 1 bus route and Bucket must arrive by day D = 1.
She could:
Take the 1st bus on day 1 (X1 = 1).

--------------Solution-------------
To find the latest time we can leave, first start with the lastest possilbe
time Bucket can arrive. To do this, find the remainder of the last route
divided into D (D%X[n]). The last day Bucket can arrive is D - (D % X[n]).
Repeat this process now with D - (D % X[n]) as the new last day bucket can arrive.
D[n-1] = D[n] - (D[n] % X[n]).

Lastly, D[1] will be the latest day Bucket can take the first bus, thus giving
the answer to the problem. 
"""

rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))
"""
def create_matrix(bus_routes,N,D):

    route_matrix = [[] for i in range(N)]

    for r in range(N):
        for x in range(1,D+1):
            if x%bus_routes[r] == 0:
                route_matrix[r].append(1)
            else:
                route_matrix[r].append(0)



    return route_matrix

def find_route(route_matrix,N,D):

    x = D-1
    y = N-1

    while y > 0:

        if x == 0:
            return 1

        if route_matrix[y][x] == 0:
            x -= 1

        if route_matrix[y][x] == 1:
            if route_matrix[y-1][x] == 1:
                y -= 1
            elif route_matrix[y-1][x-1] == 1:
                x -= 1
                y -= 1
            else:
                x -= 1

    return x+1
"""
def solve(bus_routes,N,D):

    route_tracker = N-1
    distance_tracker = D


    for route_tracker in range(N-1,-1, -1):

        distance_tracker = distance_tracker - distance_tracker%bus_routes[route_tracker]


    return distance_tracker



test_cases = rri()

for t in range(1,test_cases+1):

    N,D = rrm()
    bus_routes = rrm()


    print("Case #{}: {}".format(t,solve(bus_routes,N,D)))

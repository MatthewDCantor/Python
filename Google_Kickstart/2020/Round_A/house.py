"""
-----------Problem----------
There are N houses for sale. The i-th house costs Ai dollars to buy.
You have a budget of B dollars to spend.

What is the maximum number of houses you can buy?

------Input-------
'3'
'4 100'
'20 90 40 90'
'4 50'
'30 30 10 10'
'3 300'
'999 999 999'
--------OUTPUT-----
Case #1: 2
Case #2: 3
Case #3: 0
"""

rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))

def solve(N,B,A):
    A.sort()
    if A[0] > B:
        return 0

    ans = 0
    total = 0

    while ans < N and total + A[ans] <= B:
        total += A[ans]
        ans += 1



    return ans



"""
-----Main------
"""

t = rri()

for tc in range(1,t+1):
    N,B = rrm()
    A = rrm()
    ans = solve(N,B,A)

    print("Case #{}: {}".format(tc, ans))

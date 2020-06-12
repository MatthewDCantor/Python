""" -------Problem--------
Tambourine has prepared a fitness program so that she can become more fit.
The program is made up of N sessions and during the ith session, Tambourine
will exercise for M[i] minutes. The number of minutes she exercises in each
session is strictly increasing. The difficulty of the program is the maximum
difference between any two consecutive sessions.

K sessions can be added anywhere in the program. What is the minimum difficulty
possible after adding K or less programs.

----------Input Format-----------
Testcases
N K
M[i]

----------Sample Input and Output--------
'1'
'3 1'
'100 200 230'

Output:

Case #1: 50

'3'
'5 2'
'10 13 15 16 17'
'5 6'
'9 10 20 26 30'
'8 3'
'1 2 3 4 5 6 7 10'

Output:

Case #1: 2
Case #2: 3
Case #3: 1


------Naive Solution-------


The naive way of solving this problem would be to find the difference, D[i] between each
session and sort for max D[i]. Then we would add (M[i]+ M[i+1])/2
to the program, thus lowering the maximum difference (unless there D_max[i] == D_max[j]).
We could repeat this process K times to find the minimum difficulty.

O(nlogn * n * k ) ----> sort = O(nlogn) max = O(n) repeated K times

For the example above, this would look like:

M[i] = [100,200,230]
D[i] = [100,30]

Since 100 is the maximum, we would put a new session inbetween those:

M[i] = [100,150,200,230]
D[i] = [50,50,30]

Notice that by adding a session in between the other videos, the sum total of
D[i] doesnt change.


-------------Faster Solution----------
When K is greater than 1, placing a new session directly in the middle is not
always the most efficient solution as is show below:

                                    K = 2
              [10,20]                                   [10,20]
            [10,15,20]                                 [10,13,20]
           [10,13,15,20]                              [10,13,16,20]
           difficulty = 5                             difficulty = 4

Instead, the difference must be as evenly divided by videos K as possible.

D[i]/(K+1) = Optimal difficulty

However, K and D are integers, the optimal difficulty is:

D[i]/(K[i]+1) = ceiling(D_op)

However, this must be tested for all N-1 in D[i] while maintaining that the
sum of K[i] is less than K. Solving for K[i]:

ceiling(D[i]/d_op) - 1 = k[i]

As d_op decreases, k[i] decreases. Therefore, the maximum d_op that makes
k_sum <= K will be the answer. This can be done with a binary search.

Binary Search:
1. Begin with guess for D_op as D_max = M[-1] - M[0]
2. Go through range(N-1) and sum k[i] for the D_op guess.


"""

rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))

def solve(M,K,N):

    

    def try_op(target):

        k_sum = 0
        for i in range(N-1):
            d = M[i+1] - M[i]

            # d//target = ceiling(d/d_op) - 1 if d%target != 0

            if d%target == 0:
                k_sum += (d/target) - 1
            else:
                k_sum += d//target

        return k_sum <= K

    lo = 1
    hi = M[-1]- M[0]

    while lo < hi:
        mid = (lo+hi)//2

        if try_op(mid):

            hi = mid

        else:
            lo = mid + 1


    return lo

test_cases = rri()

for t in range(1,test_cases+1):
    n,k = rrm()
    m = rrm()

    ans = solve(m,k,n)
    print "Case #" + str(t) + ": " + str(ans)

"""
m = [[100,200,230],[10,13,15,16,17],[9,10,20,26,30],[1,2,3,4,5,6,7,10]]
k = [1,2,6,3]

ans = [50,2,3,1]

for i in range(0,4):

    print str(i+1) + ": " + str(solve(m[i],k[i],len(m[i]))) + "| Expected: " + str(ans[i])
"""

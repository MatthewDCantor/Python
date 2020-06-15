"""------------Problem---------------

Li has planned a bike tour through the mountains of Switzerland. His tour consists of N checkpoints, numbered from 1 to N in the order he will visit them. The i-th checkpoint has a height of Hi.

A checkpoint is a peak if:
It is not the 1st checkpoint or the N-th checkpoint, and
The height of the checkpoint is strictly greater than the checkpoint immediately before it and the checkpoint immediately after it.

Please help Li find out the number of peaks.


---------------Input & Output---------------
'4'
'3'
'10 20 14'
'4'
'7 7 7 7'
'5'
'10 90 20 90 10'
'3'
'10 3 10'


Case #1: 1
Case #2: 0
Case #3: 2
Case #4: 0


------------Solution--------------------

Go through array, A, in range (1,N-1) and compare A[i-1] and A[i+1] to A[i].
if A[i] > A[i-1] and A[i] > A[i+1] then A[i] is a peak.








"""


rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))

def solve(array,N):

    answer = 0

    for i in range(1, N-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            answer += 1

    return answer


test_cases = rri()

for t in range(1, test_cases+1):

    N = rri()
    hills = rrm()

    print("Case #{}: {}".format(t,solve(hills,N)))

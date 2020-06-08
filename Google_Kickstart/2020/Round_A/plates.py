"""  ------- Problem --------

N stacks of K plates with each plate having a beauty value B.

Choose P plates to maximize the sum of the beauty value. If you choose a plate
in a stack then you must choose all the plates above that plate.

------- Algorithm ------
1. create matrix that contains the sum of i plates in each stack

10 10 100 30        -original stacks
80 50 10 50

10 20 120 150       -sum stacks
80 130 140 190

2. create max value matrix, m, for the stacks where the number of plates is the
weight in a knapsack problem. Ordinarily in a knapsack 0-1 problem, we check
if adding the item in line i will add to the overall maximum. In this problem,
we must check whether sum[i][x], with x E [0,j] will add to the overall maximum.
This is basically like adding an extra dimension to the knapsack 0-1 problem,
adding an extra k to the run time (O(n*p*k))

3. Lastly, return m[n][p] for the answer



-------- input --------




'2'
'2 4 5'
'10 10 100 30'
'80 50 10 50'
'3 2 3'
'80 80'
'15 50'
'20 10'

"""





rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))

def modified_knapsack(stacks,max_plates,stack_size,plates_sum):

    # create blank max value matrix to be filled
    m = [[0 for x in range(max_plates+1)] for y in range(stacks+1)]

    #fill max value matrix

    for i in range(1,stacks+1):
        for j in range(0,max_plates+1):
            for x in range(min(j+1,stack_size+1)):
                    m[i][j] = max(plates_sum[i-1][x] + m[i-1][j-x], m[i][j])


    return m[stacks][max_plates]



def solve():

        #get n,k,p and initialize lists

        n,k,p = rrm()
        plates = []
        plates_sum = []

        #create plate stack matrix

        for i in range(n):
            plates.append(rrm())
            plates_sum.append([0])

        #create sum matrix

        for i in range(n):
            for j in plates[i]:
                plates_sum[i].append(plates_sum[i][-1] + j)



        #run the modified_knapsack algorithm on the plates_sum matrix

        ans = modified_knapsack(n,p,k,plates_sum)

        return ans

test_cases = rri()

for t in range(test_cases):

    print("Case #: " + str(t+1)+ " " + str(solve()))

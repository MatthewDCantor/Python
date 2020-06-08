"""
------------ Summary --------------
Minimize the maximum delivery time of a package in a matrix RxC where,
1 = delivery office
0 = no delivery office
by adding one delivery office.


The time to deliver a package is considered to be the manhattan distance
from the nearest delivery office.

manhattan distance --> |x2 - x1| + |y2 - y1|

------------ Sample Input & Output ------------
3         T = 3
3 3       R,C = 3
101
000   ==> Matrix --> odm (original delivery matrix)
101
1 2       R = 1, C = 2
11    ==> Matrix
5 5   ==> R,C = 5
10001
00000
00000 ==> Matrix
00000
10001

Case #1: 1
Case #2: 0
Case #3: 2
Case #4: 2

'4'
'3 3'
'101'
'000'
'101'
'1 2'
'11'
'5 5'
'10001'
'00000'
'00000'
'00000'
'10001'
'12 5'
'00010'
'01001'
'00000'
'01100'
'01111'
'00000'
'00000'
'00000'
'11111'
'11111'
'00000'
'01110'
"""


import numpy as np
import queue
import time
import sys
sys.setrecursionlimit(2000)




def find_ones(mat):
    ones = []
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):

            if mat[i,j] == 1:
                ones.append((i,j))
    return ones


def MS_BFS(matrix):

    ones = find_ones(matrix)
    q = queue.Queue()

    for i in ones:
        q.put(i)

    spt = set()
    dist = [[] for i in range(matrix.shape[0])]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if (i,j) in ones:
                dist[i].append(0)
            else:
                dist[i].append("NA")


    while(q.empty() != True):

        k = q.get()
        spt.add(k)



        for i in range(k[0]-1, k[0]+2):
            if (i,k[1]) not in spt and -1 < i < matrix.shape[0]:
                q.put((i,k[1]))
                if dist[i][k[1]] == "NA":
                    dist[i][k[1]] = dist[k[0]][k[1]] + 1

        for j in range(k[1]-1, k[1]+2) :
            if (k[0],j) not in spt and -1 < j < matrix.shape[1]:
                q.put((k[0],j))
                if dist[k[0]][j] == "NA":
                    dist[k[0]][j] = dist[k[0]][k[1]] + 1

    return dist

""" ----- MAIN ------ """

T = int(input())

for t in range(T):
    R,C = list(map(int, input().split(' ')))

    mat = np.matrix([list(map(int ,list(input()))) for i in range(R)])
    manhattan_distance = MS_BFS(mat)
    ans = max([max(i) for i in manhattan_distance])


    ones = find_ones(mat)


    for y in range(R):
        for x in range(C):
            if (y,x) not in ones:
                mat[y,x] = 1
                manhattan_distance = MS_BFS(mat)
                ans = min(max([max(i) for i in manhattan_distance]), ans)
                mat[y,x] = 0






    print("Case #" + str(t+1) + ': ' + str(ans))

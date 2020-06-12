

"""
This algorithm finds the distance from any point to the nearest source in O(rowxcol) time


"""

import numpy as np
import queue
import time
import sys
sys.setrecursionlimit(2000)

n = 5
matrix = np.zeros((n,n))

matrix[3,3],matrix[3,2],matrix[3,0], = 1,1,1


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




    """
    for n in range(current_x-1,current_x+1):
        for m in range(current_y-1,current_y+1):
            if not (n==current_x and m==current_y) \
                and n>-1 and m>-1 \
                and n<matrix.shape[0] and m<matrix.shape[1] \
                and (n,m) not in queue.queue :
                    queue.put((n,m))
    return BFS(matrix,queue)
    """

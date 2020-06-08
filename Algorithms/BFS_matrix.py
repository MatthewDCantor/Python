

"""
1. Pick any node, visit the adjacent unvisited vertex,
mark it as visited, display it, and insert it in a queue.
2. If there are no remaining adjacent vertices left,
remove the first vertex from the queue.
3. Repeat step 1 and step 2 until the queue
is empty or the desired node is found.
"""

import numpy as np
import queue
import time
import sys
sys.setrecursionlimit(2000)

n = 15
matrix = np.zeros((n,n))

matrix[3,3] = 1

def BFS(matrix, queue=None):

        current_index = queue.get()
        current_x,current_y = current_index[0],current_index[1]

        element = matrix[current_y,current_x]

        if element == 1: return current_x,current_y

        for n in range(current_x-1,current_x+2):
            for m in range(current_y-1,current_y+2):
                if not (n==current_x and m==current_y) \
                    and n>-1 and m>-1 \
                    and n<matrix.shape[0] and m<matrix.shape[1] \
                    and (n,m) not in queue.queue :
                        queue.put((n,m))
        return BFS(matrix,queue)
start_x,start_y = 6,8

start_queue = queue.Queue()
start_queue.put((start_x,start_y))
BFSstart = time.time()
BFS_results = BFS(matrix ,start_queue)
BFSend = time.time()

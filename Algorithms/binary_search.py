"""
-------------Binary Search Algorithm-------------

We basically ignore half of the elements just after one comparison.

1. Compare x with the middle element.
2. If x matches with middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
4. Else (x is smaller) recur for the left half.
"""

def binary_search(array,target,low,high):

        if low < high:

            mid = (low + (high-1))//2

            if array[mid] == target:
                return mid

            elif array[mid] < target:
                return binary_search(array,target,mid+1,high)

            else:
                return binary_search(array,target,low,mid-1)
        elif low == high:
            if array[low] == target:
                return low

            else:
                print "Target not found!"


arr = [1,2,3,4,5,6,7,8,9,10]

""" Ceiling Binary Search

This algorithm finds the element in the array which is closest to the target and
greater than or equal to the target.

If target = 8 and array = [2,3,6,9,10] then the algorithm would return 9.


1. If array[0] > target then return 0
2. if array[-1] < target then return no ceiling
3. Compare target with the middle element.
4. If target matches with middle element, we return the mid index.
5. If target < array[mid] then check two conditions:
    i. if array[mid-1] < target then mid is ceiling.
    ii. else we return the binary search with the bottom half of the array.
6. If target > array[mid] then check two conditions:
    i. if array[mid+1] > target then mid+1 is ceiling.
    ii. else we return the binary search with the top half of the array.


"""


def ceil_binary_search(array,target,low,high):

    #1
        if array[0] >= target:
            return 0
    #2
        if array[-1] < target:

            return

        if low < high:

            mid = (low + (high-1))//2
    #3&4
            if array[mid] == target:
                return mid
    #5
            elif array[mid] > target:
                if array[mid-1] < target:
                    return mid
                else:
                    return ceil_binary_search(array,target,low,mid-1)
    #6
            elif array[mid] < target:

                if array[mid+1] >= target:
                    return mid+1

                else:
                    return ceil_binary_search(array,target,mid+1,high)



        elif low == high:
            if array[low] == target:
                return low


arr = [1,2,3,8,9,10,14]

for i in range(16):
    print ["target:" + str(i),arr[ceil_binary_search(arr,i,0,len(arr))]]

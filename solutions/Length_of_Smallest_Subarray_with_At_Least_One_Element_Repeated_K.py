"""
Given an array arr[] of length N and an integer K. 
The task is to find the minimum length of subarray such that at least one element of the subarray is repeated exactly K times in that subarray. 
If no such subarray exists, print -1
"""

def findSubarray(arr, k):
    # Brute Force: nested for-loop to generate all subarrays
    # frequency count check if there is one with K counts, compare length
    # TC: O(n^2) | SC: O(n)
    # n = len(arr)
    # min_len = float('inf')
    # for i in range(n):
    #     count = 0
    #     for j in range(i, n):
    #         if arr[j] == arr[i]:
    #             count += 1
    #         if count == k:
    #             min_len = min(min_len, j - i + 1)

    # return min_len if type(min_len) == int else -1

    # Improved: Iterate the array, store index location of the elements if does not exist
    # Otherwise, take difference at the length, update with current index value (find shortest)
    n = len(arr)
    min_len = float('inf')
    counter = {}
    for i in range(n):
        if arr[i] not in counter:
            counter[arr[i]] = [i, 1] # first occurence index, count
        else:
            counter[arr[i]][1] += 1

        if counter[arr[i]][1] == k:
            min_len = min(min_len, i - counter[arr[i]][0] + 1)

    return min_len



    # return min_len

# arr = [1, 2, 1, 2, 1]
# k = 2

# arr = [2, 2, 2, 3, 4]
# k = 3

# arr = [0 ,1, 2, 2, 1, 2, 1, 1]
# k = 1

arr = [1, 3, 7, 6, 2, 1, 4, 5]
k = 2


print(findSubarray(arr, k))


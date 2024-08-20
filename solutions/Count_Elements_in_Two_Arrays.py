def countElements(arr1, arr2):
    # Problem: For each element in array 1, count elements less than or equal to it in array 2
    # Brute Force: Nested for-loops TC: O(N^2) | SC: O(N)

    # Improvement: Sort + Binary Search TC: O( N log N) | SC: O(N)
    arr2.sort()
    res = []
    for x in arr1:
        # print(f"x={x}")
        cnt = 0
        l, r = 0, len(arr2) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr2[mid] <= x:
                # print(f"{arr2[mid]} smaller than {x}")
                cnt += len(arr2[l:mid+1])
                # print(cnt)
                l = mid + 1
            else:
                r = mid-1
        res.append(cnt)
        cnt = 0

    return res


    
arr1 = [1, 2, 3, 4, 7, 9]
arr2 = [0, 1, 2, 1, 1, 4] # [0, 1, 1, 1, 2, 4]

print(countElements(arr1, arr2))
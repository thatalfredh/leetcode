from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)
        # look up to determine if option 3 is a possible jump
        lookup = {}
        for i in range(n):
            if arr[i] not in lookup.keys():
                lookup[arr[i]] = set()
            lookup[arr[i]].add(i)

        # notice for example 1: [100,-23,-23,404,100,23,23,23,3,404]
        # take option of i + 1 at index 0: next index = 1
        # at index 1: we have option of 1 - 1 = 0; this creates exploration of the same thing infinitely
        # thus visit marks what we do not want to try again while we have yet to converge to solution
            
        visit = [0 for _ in range(n)]

        # at every index, we have three choices to make:
        # +1, -1, +j where arr[i] == arr[j]
        # if there exists multiple arr[i] == arr[j], we also want to try them all
        # only by trying will we know which ones are not part of optimal solution

        def f(idx, visit, memo):
            # as we are finding minimized solution, return INF means the result from this call can never be part of optimal solution
            if idx >= n or idx < 0 or visit[idx] == 1:
                return float("inf")
            if idx == n-1: # goal reached
                return 0
            visit[idx] = 1
            # local copy for each recursive call so that we "backtrack"
            # otherwise the base case will be prematurely encountered in other recursive calls
            option_1 = 1 + f(idx + 1, visit.copy())
            option_2 = 1 + f(idx - 1, visit.copy())
            option_3 = float("inf")
            # similarly, if some indices of the duplicated values have been tried (but still no solution), we treat them as INF
            if arr[idx] in lookup.keys():
                option_3 = 1 + min(
                    [
                        f(x, visit.copy()) if (
                            visit[x] == 0
                        ) else (
                            float("inf")
                        ) for x in lookup[arr[idx]] 
                    ]
                )
            return min(option_1, option_2, option_3)

        return f(0, visit)



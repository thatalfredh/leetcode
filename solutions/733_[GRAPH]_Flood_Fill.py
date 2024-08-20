from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image) # rows
        n = len(image[m-1]) # cols

        # intuition: we can start from anywhere specified by (sr, sc)
        # we check surrounding for the same color, change it if same and explore
        # otherwise, ignore

        # intuition: we can consider BF recursion but we would also encounter the same neighbour
        visited = set()
        nodes = m*n
        neighbours = {}
        for i in range(nodes):
            a = i // m
            b = i % n
            neighbours[i] = []
            if (a - 1) >= 0: # up
                neighbours[i].append(i-m)
            if (a + 1) <= (m - 1): # down
                neighbours[i].append(i+m)
            if (b - 1) >= 0: # left
                neighbours[i].append(i-1)
            if (b + 1) <= (n - 1): # right
                neighbours[i].append(i+1)

        print(neighbours)
        c = image[sr][sc] # initial colour
        def explore(image, a, b, c, color):
            if (a*m + b) not in visited:
                visited.add(a*m + b) # add node to visited
                print(visited)
                # print(a*m+b)
                # print(a)
                # print(b)
                # print("---")
                if image[a][b] == c:
                    image[a][b] = color # change color
                    for nbr in neighbours[a*m + b]:
                        # print(neighbours[a*m+b])
                        # print(nbr//m , nbr %n)
                        explore(image, nbr // m, nbr % n, c, color) 
                
        explore(image, sr, sc, c, color)


        return image


sol = Solution()

# image = [[1,1,1],[1,1,0],[1,0,1]]
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
sol.floodFill(image, sr, sc, color)

print(image)



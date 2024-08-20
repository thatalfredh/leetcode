# from collections import defaultdict, deque

# stack = deque([])

# stack.append(0)

# stack[-1]

# stack.append(1)

# print(stack)

def dfs(node, visit):
    visit[node] = 1
    print(node, visit)
    if len(graph[node]) == 1 and visit[graph[node][0]] == 1:
        return [node]
    else:
        paths = []
        for child in graph[node]:
            if visit[child] == 0:
                child_path = dfs(child, visit)
                paths.append(child_path)
        # print(paths)
        return [node] + max(paths, key=len)


edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

graph = {
    0: [3],
    1: [3],
    2: [3],
    3: [0, 1, 2, 4],
    4: [3, 5],
    5: [4]
}
visit = [0 for _ in range(6)]
print(dfs(2, visit))
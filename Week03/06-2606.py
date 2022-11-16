from collections import deque

def bfs(x: int = 1) -> int:

    queue = deque()
    queue.append(x)
    visited[x] = True
    
    result = 0

    while queue :
        p = queue.popleft()

        for i in graph[p]:
            if not visited[i]:
                result += 1
                visited[i] = True
                queue.append(i)


    return result

computers = int(input())
connected = int(input())

visited = [False] * (computers + 1)
graph = [[] for _ in range(computers + 1)]

for _ in range(connected):
    start, dest = map(int, input().split())
    graph[start].append(dest)
    graph[dest].append(start)

print(bfs())




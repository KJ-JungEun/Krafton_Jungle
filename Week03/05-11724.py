def dfs(x: int) -> None:
    check[x] = True
    for next in graph[x]:
        if not check[next]:
            dfs(next)
    return

n, m = map(int, input().split())

check = [False for i in range(n+1)]
graph = [[] for i in range(n+1)]
ans = 0

for _ in range(m):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)


for i in range(1, n + 1):
    if not check[i]:
        dfs(i)
        ans += 1

print(ans)
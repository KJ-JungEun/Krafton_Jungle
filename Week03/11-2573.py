
iceburg =  [[0, 0, 0, 0, 0, 0, 0],
            [0, 2, 4, 5, 3, 0, 0],
            [0, 3, 0, 2, 5, 2, 0],
            [0, 7, 6, 2, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
n,m = 5,7
melt = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)]for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
for x in range(n):
    for y in range(m):

        if  iceburg[x][y] > 0:
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if x>0 or y>0 or n>=x or m>=y :

                    if iceburg[nx][ny] == 0:
                        melt[x][y] -= 1

for i in range(n):
    for j in range(m):
        iceburg[i][j] += melt[i][j]

melt = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    print(iceburg[i])
print('-----------------------------')
for i in range(n):
    print(melt[i])
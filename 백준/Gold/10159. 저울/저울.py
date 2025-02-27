import sys
input = sys.stdin.readline
INF = int(10e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int,input().split())
  graph[a][b] = 1

for k in range(1, n+1):
  graph[k][k] = 0
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1, n+1):
  cnt = 0
  for j in range(1, n+1):
    if i != j and graph[i][j] == INF and graph[j][i] == INF:
      cnt += 1
  print(cnt)
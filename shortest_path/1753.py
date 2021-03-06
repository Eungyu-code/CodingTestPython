
import heapq

INF = int(1e9)
v, e = map(int, input().split())
k = int(input())
arr = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))


def dijkstra():
    q = []
    heapq.heappush(q, (0, k))
    distance[k] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()
for a in range(1, v + 1):
    if distance[a] == INF:
        print("INF")
    else:
        print(distance[a])
import heapq
from naive_dijkstras import graph
from numpy import Inf

def lazy_dijkstras(graph, root):
    n = len(graph)
    dist = [Inf for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    pq = [(0, root)]
    while len(pq) > 0:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))
    return dist

lazy_dijkstras(graph, 1)
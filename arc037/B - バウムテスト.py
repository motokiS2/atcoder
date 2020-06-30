n, m = map(int, input().split())

graph = [[-1] * n] * n

# for i in range(m):
#     u, v = map(int, input().split())
#     graph[u - 1] = v - 1
#     graph[v - 1] = u - 1


print(graph)
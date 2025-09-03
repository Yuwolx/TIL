import heapq


def dijstra(start_point):
    # start
    inf = 10**10
    distance = [inf for _ in range(vertex + 1)]
    distance[start_point] = 0
    plans = [(distance[start_point],start_point)]
    while plans:
        dist, node = heapq.heappop(plans)
        if dist > distance[node]: continue

        for w, e in idj_list[node]:
            if dist + w < distance[e]:
                distance[e] = dist + w
                heapq.heappush(plans,(distance[e],e))
    return distance


vertex, edge = map(int, input().split())

idj_list = [[] for _ in range(vertex+1)]
for _ in range(edge):
    s,e,w = map(int, input().split())
    idj_list[s].append((w,e))
    idj_list[e].append((w,s))

# for x in idj_list:
#     print(x)

x, y = map(int, input().split())

ss = dijstra(1)
sx = dijstra(x)
sy = dijstra(y)
middle = sx[y]
x_in = ss[x] + sy[vertex]
y_in = ss[y] + sx[vertex]

result = middle + min(x_in, y_in)
if result >= 10**10:
    print(-1)
else:
    print(result)
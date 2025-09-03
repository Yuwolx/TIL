import heapq

vertexs, edges = map(int, input().split())

start_point = int(input())

edge_list = []
for _ in range(edges):
    start, end, weight = map(int, input().split())
    edge_list.append([start,end, weight])

# make ifdj list
idj_list = [[] for _ in range(vertexs+1)]

for s, e, w in edge_list:
    idj_list[s].append([e,w])

# make distance
INF = 20000*100
distance = [INF for _ in range(vertexs+1)]
# starting point to itself's distance is 0
distance[start_point] = 0
#print(f'distance: {distance}')

# make heapq for visit
plans = []
heapq.heappush(plans, (distance[start_point],start_point))

while plans:
    dist, node = heapq.heappop(plans)
    # if exceed previous dist, then dismiss
    if dist > distance[node]: continue

    # visit idj node
    for e, w in idj_list[node]:
        #print(f'e,w: {e, w}')
        if dist + w < distance[e]:
            distance[e] = dist + w
            heapq.heappush(plans, (distance[e],e))




for y in range(1,len(distance)):
    if distance[y] == INF:
        print('INF')
    else:
        print(distance[y])
# for x in idj_list:
#     print(x)


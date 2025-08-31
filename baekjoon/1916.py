import heapq

def dikstra(idj_list, start, end):
    # make distance
    inf = 10**10
    distance = [inf for _ in range(vertex+1)]
    distance[start] = 0
    # print(f'distance: {distance}')

    plans = []
    heapq.heappush(plans, (distance[start], start))

    while plans:
        # print(f'plans: {plans}')
        dist, ctn = heapq.heappop(plans)

        if distance[ctn] < dist: continue

        for w, e in idj_list[ctn]:
            if dist + w < distance[e]:
                distance[e] = dist + w
                heapq.heappush(plans, (distance[e], e))

    return distance[end]



vertex = int(input())
# print(f'vertex: {vertex}')
edges = int(input())
# print(f'edges: {edges}')

edge_list = []
for _ in range(edges):
    s, e, w= map(int, input().split())
    edge_list.append([s,e,w])

# print(f'edge list: {edge_list}')

start, end = map(int, input().split())
# print(f'start, end: {start, end}')

#make idj list
idj_list = [[] for _ in range(vertex+1)]
for s, e, w in edge_list:
    idj_list[s].append([w,e])

# print('idj list')
# for i in idj_list:
#     print(i)

result = dikstra(idj_list, start, end)
    

print(result)




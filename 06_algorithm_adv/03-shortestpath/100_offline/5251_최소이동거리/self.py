import sys, heapq
sys.stdin = open('input.txt')

import heapq

def dijkstra(end_point, starting_point):
    # make minimum distance from 0
    inf = 10**10
    distance = [inf for _ in range(end_point+1)]

    distance[starting_point] = 0
    plans = []
    heapq.heappush(plans, (distance[starting_point], starting_point))

    while plans:
        dist, end = heapq.heappop(plans)
        # print(f'dist, end: {dist, end}')
        if distance[end] < dist: continue

        for e, w in idj_list[end]:
            # print(f'e,w: {e,w}')
            if dist + w < distance[e]:
                distance[e] = dist + w
                heapq.heappush(plans, (distance[e], e))

    return distance


T = int(input())
for tc in range(1,T+1):
    end_point, edges = map(int, input().split())
    
    edge_list = []
    for _ in range(edges):
        start, end, weight = map(int,input().split())
        edge_list.append([start,end,weight])

    # print(f'end_point, edges: {end_point, edges}')
    # print('edge list')
    # for i in edge_list:
    #     print(i)

    #make idj list
    idj_list = [[] for _ in range(end_point+1)]
    for s, e, w in edge_list:
        idj_list[s].append([e,w])
    
    # # print('idj list')
    # for x in idj_list:
    #     print(x)

    result = dijkstra(end_point,0)[end_point]
    print(f'#{tc} {result}')
    






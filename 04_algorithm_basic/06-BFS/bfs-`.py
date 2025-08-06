



graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E','F'],
    'C': [],
    'D': ['G', 'H', 'I'],
    'E': [],
    'F': [],
    'G': []
}


def BFS(root_node):

    #parameter: root of subtree who start BFS
    result = []
    data_structure = [root_node]
    # explore finish when I have been searchin every nodes
    while data_structure: # There are candidiates keep going
    #node = data_structure.pop() # LILO mean DFS
        node = data_structure.pop(0) #FIFO
        result.append(node)
        # find my child node 
        for child in graph.get(node, []): #get method defauitly have key value
                                        # There no key to find, return empty list
            # insert my kds to next visit candidates group 
            data_structure.append(child)

    return result

print(BFS('A'))



#Graph

#make adj_list
nodes = range(7)

# 간선 정보
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 4),
    (3, 5),
    (4, 5),
    (5, 6)
]

# 인접 리스트 초기화
adj_list = {node: [] for node in nodes}

# 간선 정보로 인접 리스트 채우기
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)  # 방향 없으니까 둘 다

# 결과 출력
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")




"""

          0
        /   \
       1     2
     /   \     \
    3     4     \
     \   /        \
       5 <----------
        |
        6
"""
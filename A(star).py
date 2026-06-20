import heapq

def A_star():
    node_num, edge_num =  input().split()
    node_num, edge_num = int(node_num), int(edge_num)
    graph={}
    for i in range(0,edge_num):
        u,v,w= input().split()
        if u not in graph.keys():
            graph[u]=[]
        graph[u].append((v,int(w)))
    heuristics = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0 }

    pq=[]
    heapq.heappush(pq,(heuristics['A'],'A',0))
    visited=[]
    while pq:
        h,node,g=heapq.heappop(pq)
        if node in visited:
            continue
        if node not in visited:
            visited.append(node)
        if node == "G":
            print(g)
            return
        if node not in graph.keys():
            continue
        for n,w in graph[node]:
            if n not in visited:
                temp_g=g+w
                new_f=temp_g+ heuristics[n]
                heapq.heappush(pq,(new_f,n,temp_g))
    print("-1")

A_star()

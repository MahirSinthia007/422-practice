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
    heapq.heappush(pq,(heuristics['A'],'A',))

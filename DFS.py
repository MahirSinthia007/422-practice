from collections import deque
start='A'
stack=deque()
stack.append(start)
visited=set()
goal="G"
path=""
graph={}
while stack:
    node=stack.pop()
    if node in visited:
        continue
    else:
        visited.add(node)
    if node==goal:
        print(path)
        break
    for n ,w in graph[node]:
        if n not in visited:
            new_path=path+n
            stack.append(n)



    
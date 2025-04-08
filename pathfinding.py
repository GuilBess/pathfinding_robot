from __future__ import annotations

class Node:
    #Each node has connected nodes (conn), meaning an adjacent node is reachable
    #The path is used when exploring the solutions
    def __init__(self, id: int, conn:list[int] = [], path:list[int] = []):
        self.id = id
        self.conn = conn
        self.path = path

    def __str__(self):
        return str(self.id)

row = 10
col = 10

nodes: list[Node] = []
for i in range(row):
    for j in range(col):
        conn =  []
        if (i-1) * col + j >= 0:
            conn.append((i-1) * col + j)
        if j > 0:
            conn.append(i * col + j - 1)
        if j < col-1:
            conn.append(i * col + j + 1)
        if (i + 1) * col < row*col -1:
            conn.append((i + 1) * col + j)
        nodes.append(Node(i*col+j, conn))



# BFS recursive function for path finding
def find_path(stop: int, n: list[Node], step: int = 0) -> list[str]:
    print(step)
    for i in n:
        if i.id == stop:
            return i.path + [i.id]
    
    new_n: list[Node] = []
    for i in n:
        for j in i.conn:
            if i.id != j and j not in i.path:
               
                new_n.append(Node(j, nodes[j].conn, i.path + [i.id])) 
    return find_path(stop, new_n, step + 1)

print(find_path(75, [nodes[0]]))
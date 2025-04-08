import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import time

class Node:
        #Each node has connected nodes (conn), meaning an adjacent node is reachable
        #The path is used when exploring the solutions
        def __init__(self, id: int, conn:list[int] = [], path:list[int] = []):
            self.id = id
            self.conn = conn
            self.path = path

        def __str__(self):
            return str(self.id)

class Pathfinding:
    # We now assume we get the maze as a 2D array with descriptions of the walls as input
    # Array should look like  [["tl", "tb", "tr",...],[...],...]
    # letters define if there are walls (t = top, b = bottom, l = left, r = right)
    def __init__(self):
        pass
        
    def __arr2graph(self, maze:list[list[str]]) -> None:
        row = len(maze)
        col = len(maze[1])

        nodes: list[Node] = []
        for i, l in enumerate(maze):
            for j, walls in enumerate(l):
                conn =  []
                if (i-1) * col + j >= 0 and "t" not in walls:
                    conn.append((i-1) * col + j)
                if j > 0 and "l" not in walls:
                    conn.append(i * col + j - 1)
                if j < col-1 and "r" not in walls:
                    conn.append(i * col + j + 1)
                if (i + 1) * col < row*col -1 and "b" not in walls:
                    conn.append((i + 1) * col + j)
                nodes.append(Node(i*col+j, conn))
        self.nodes = nodes
    

    # BFS recursive function for path finding
    def __find_path(self, stop: int, n: list[Node], step: int = 0) -> list[int]:
        for i in n:
            if i.id == stop:
                return i.path + [i.id]
        
        new_n: list[Node] = []
        for i in n:
            for j in i.conn:
                if i.id != j and j not in i.path:
                
                    new_n.append(Node(j, self.nodes[j].conn, i.path + [i.id])) 
        return self.__find_path(stop, new_n, step + 1)

    def get_path_from_maze(self, maze: list[list[str]], start: int, stop: int) -> list[int]:
        self.__arr2graph(maze)
        return self.__find_path(stop, [self.nodes[start]])
    
    def draw_maze(self, maze: list[list[str]], path: list[int] = None):
        rows = len(maze)
        cols = len(maze[0]) if rows > 0 else 0

        fig, ax = plt.subplots(figsize=(cols, rows))
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)
        ax.set_aspect('equal')
        ax.invert_yaxis()  # So (0,0) is at top-left
        ax.axis('off')

        # Draw each cell's walls
        for y in range(rows):
            for x in range(cols):
                cell = maze[y][x]
                cell_number = y * cols + x

                if cell_number in path:
                    if path[0] == cell_number:
                        ax.add_patch(plt.Rectangle((x, y), 1, 1, color='blue', alpha=0.3))
                    elif path[-1] == cell_number:
                        ax.add_patch(plt.Rectangle((x, y), 1, 1, color='green', alpha=0.3))
                    else:
                        ax.add_patch(plt.Rectangle((x, y), 1, 1, color='red', alpha=0.3))

                # Top wall - draw gray line first, then black if wall exists
                ax.add_line(Line2D([x, x+1], [y, y], color='gray', linewidth=0.5, alpha=0.5))
                if 't' in cell:
                    ax.add_line(Line2D([x, x+1], [y, y], color='black', linewidth=2))

                # Bottom wall
                ax.add_line(Line2D([x, x+1], [y+1, y+1], color='gray', linewidth=0.5, alpha=0.5))
                if 'b' in cell:
                    ax.add_line(Line2D([x, x+1], [y+1, y+1], color='black', linewidth=2))

                # Left wall
                ax.add_line(Line2D([x, x], [y, y+1], color='gray', linewidth=0.5, alpha=0.5))
                if 'l' in cell:
                    ax.add_line(Line2D([x, x], [y, y+1], color='black', linewidth=2))

                # Right wall
                ax.add_line(Line2D([x+1, x+1], [y, y+1], color='gray', linewidth=0.5, alpha=0.5))
                if 'r' in cell:
                    ax.add_line(Line2D([x+1, x+1], [y, y+1], color='black', linewidth=2))

        plt.show()

        
# Probable maze
arr = [
    ["tl", "tb", "t", "tb", "t", "tb", "tb", "trb", "tl", "t", "tr"],
    ["l", "tr", "l", "tr", "l", "t", "t", "t", "r", "l", "r"],
    ["bl", "br", "bl", "b", "b", "b", "b", "b", "br", "bl", "br"]
]

"""
# Empty maze
arr = [
    ["tl", "t", "t", "t", "t", "t", "t", "t", "t", "t", "tr"],
    ["l", "", "", "", "", "", "", "", "", "", "r"],
    ["bl", "b", "b", "b", "b", "b", "b", "b", "b", "b", "br"]
]"""

pathfinder = Pathfinding()

t = time.time()
path = pathfinder.get_path_from_maze(arr, start=0, stop=32)
print("Time for pathfinding: " + str(time.time() - t))
print(path)

pathfinder.draw_maze(arr, path)

path = pathfinder.get_path_from_maze(arr, start=10, stop=22)
pathfinder.draw_maze(arr, path)
# Pathfinding algorithm
the pathfinding algorithm works with a node graph, explored using a BFS algorithm to guarantee we have the shortest path.

This is not the most efficient way to find a path in a maze, but our maze is small enough that the worst case scenario takes around _25 ms_

Here is how the nodes are described:

- Node class: Node(id:int, conn:list[int] = [], path:list[int] = [])
- id: a unique name for a specific maze "square". defined as row_nbr * col_nbr of the square (top left square would be id 0, the square to it's right would be id 1, the square below would be id 10 etc...)
- conn: list of ids of all the nodes connected to this node. With now maze walls, this would be [1, 10] for the top left square
path: Stores the ids of the nodes we had to go through to get to this one when searching a path. Leave as default when creating the squares.

## Use the algorithm
- Throught the Pathfinding class, using an array to describe the maze:

```python
maze = [
    ["tl", "tb", "t", "tb", "t", "tb", "tb", "trb", "tl", "t", "tr"],
    ["l", "tr", "l", "tr", "l", "t", "t", "t", "r", "l", "r"],
    ["bl", "br", "b", "b", "b", "b", "b", "b", "br", "bl", "br"]
]

pathfinder = Pathfinding()

path = pathfinder.get_path_from_maze(maze, start=23, stop=32)

pathfinder.draw_maze(arr, path)
```
Here, t,b,l and r stand for top, bottom, left and right. Each cell represents a maze square, and the string describes which walls are present. For example, "tl" means the top and left wall of the square are present, and we could got to the cell on the bottom or on the right. A square marked "tblr" would be unreachable or unescapable.

The draw_maze function is used to visualize the maze. If a path from the get_path_from_maze function is given as argument, this path will be drawn on the maze too.

The maze's squares are given a number each, from left to right and top to bottom, starting top left at 0. The start and stop arguments of the get_path_from_maze function define the starting position in the maze and the desired destination square.

### the find path method
- stop: The id of the square we want to reach
- n: List of nodes where we want to start from (this will most likely be a list of one node in our case)

### get_json_from_maze method
This method takes the same parameters as the get_path_from_maze method, plus an argument "save" to choose if you want to save the json result in a file or just return it. The meaning of this is to put the data in a format all the group members understand. It is formated in thew following way:

```json
{
  "commands": [
    {
      "command": "forward",
      "args": [
        "4"
      ]
    },
    {
      "command": "rotate",
      "args": [
        "90"
      ]
    }, ...
```

the args for the "forward" command as of now is how many cells we want to go forward. The arg for the rotate command are express in degrees of clockwise rotation.

## Requierements
matplotlib: 
```bash
pip install matplotlib
```
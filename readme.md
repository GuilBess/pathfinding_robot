# Pathfinding algorithm
the pathfinding algorithm works with nodes

Here is how the nodes are described:

- Node class: Node(id:int, conn:list[int] = [], path:list[int] = [])
- id: a unique name for a specific maze "square". defined as row_nbr * col_nbr of the square (top left square would be id 0, the square to it's right would be id 1, the square below would be id 10 etc...)
- conn: list of ids of all the nodes connected to this node. With now maze walls, this would be [1, 10] for the top left square
path: Stores the ids of the nodes we had to go through to get to this one when searching a path. Leave as default when creating the squares.

## Use the algorithm
- See the example of the nodes creation (we create a row * col maze with no walls)
- Use the find_path method to search for the path: find_path(stop: int, n : list[Node]) -> list[int]
- find_path returns the optimal path, af a list of ids of the squares we have to go through

### the find path method
- stop: The id of the square we want to reach
- n: List of nodes where we want to start from (this will most likely be a list of one node in our case)

## What is left to do? 

- Make this into a class
- Implement a function to create the nodes list from the image or from a 2D array
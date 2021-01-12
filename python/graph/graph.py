from queue import Queue
# q = Queue()
# q.put(item)
# q.get()

def next_moves(graph, vertex):
    return graph[vertex]
    
    
def shortest_path_length(graph, start, end):
    # enqueue all neighbours of start
    # add all enqueued neighbours to seen dict{vertex: distance}
    
    seen = {start: 0}
    q = Queue()
    q.put(start)
    
    while not q.empty():
        vertex = q.get()
        
        for neighbour in next_moves_2(graph, vertex):
            q.put(neighbour)
            seen[neighbour] = seen[vertex] + 1
            
            if neighbour == end:
                return seen[vertex] + 1
            if neighbour in seen:
                continue
            
    
    return float('inf')


def backtrack(seen, vertex):
    moves = []
    while seen[vertex] is not None:
        moves.append(vertex)
        vertex = seen[vertex]
    
    return moves
        

def shortest_path(graph, start, end):
    # enqueue all neighbours of start
    # add all enqueued neighbours to seen dict{vertex: distance}
    
    seen = {start: None}
    q = Queue()
    q.put(start)
    
    while not q.empty():
        vertex = q.get()
        
        for neighbour in next_moves_2(graph, vertex):
            q.put(neighbour)
            seen[neighbour] = vertex
            
            if neighbour == end:
                return backtrack(seen, neighbour)
            if neighbour in seen:
                continue
            
    
    return float('inf')


if __name__ == '__main__' and False:
    graph = {
        'a' : ['b'],
        'b' : ['c',],
        'c' : ['a', 'g', 'd'],
        'd' : ['e', 'a'],
        'e' : [],
        'g' : ['d']
    }
    
    res = shortest_path(graph, 'a', 'd')
    print(res)
    assert res == 3 # ['a', 'd', 'e']

    
def next_moves_2(matrix, coordinate):
    i, j = coordinate
    # only return coordinates that are in bounds
    # and whose values in the matrix are 1
    moves = []
    
    # up
    if i > 0 and matrix[i-1][j]:
        moves.append((i-1,j))
    # down
    if i < len(matrix) -1 and matrix[i+1][j]:
        moves.append((i+1,j))
    # left
    if j > 0 and matrix[i][j-1]:
        moves.append((i, j-1))
    # right
    if j < len(matrix[0]) - 1 and matrix[i][j+1]:
        moves.append((i, j+1))
    
    return moves
    
    
if __name__ == '__main__':    
    matrix = [
        [1, 1, 1, 0],
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]

    
    # print(next_moves_2(matrix, (1, 1)))    
    
    start = (0, 0)
    end = (3, 3)
    res = shortest_path(matrix, start, end)
    print(res)
    
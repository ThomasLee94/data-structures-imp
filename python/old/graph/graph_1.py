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
        
        for neighbour in next_moves(graph, vertex):
            q.put(neighbour)
            seen[neighbour] = seen[vertex] + 1
            
            if neighbour == end:
                return seen[vertex] + 1
            if neighbour in seen:
                continue
            
    
    return float('inf')


if __name__ == '__main__':
    graph = {
        'a' : ['b'],
        'b' : ['c',],
        'c' : ['a', 'g', 'd'],
        'd' : ['e', 'a'],
        'e' : [],
        'g' : ['d']
    }
    
    res = shortest_path_length(graph, 'a', 'd')
    print(res)
    assert res == 3 # ['a', 'd', 'e']

    

    
    

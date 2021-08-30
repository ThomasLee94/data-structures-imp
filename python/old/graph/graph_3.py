# https://leetcode.com/problems/search-a-2d-matrix-ii/

from queue import Queue

def next_moves(matrix, start, target):
    # print(start)
    moves = []
    i, j = start
    
    if target > matrix[i][j]:
        if j < len(matrix[0])-1:
            moves.append((i,j+1))
        if i < len(matrix)-1:
            moves.append((i+1,j))
        
    if target < matrix[i][j]:
        if i > 0:
            moves.append((i-1,j))
        if j > 0:
            moves.append((i,j-1))
    return moves

def shortest_path(matrix, start, target):
    seen = {start: 0}
    q = Queue()
    q.put(start)
    
    while not q.empty():
        coordinate = q.get()
        print(coordinate)
        
        for neighbour in next_moves(matrix, coordinate, target):
            if neighbour in seen:
                continue

            i, j = neighbour   
            q.put(neighbour)
            seen[neighbour] = seen[coordinate]
            
            if matrix[i][j] == target:
                return True
    return False
    
def searchMatrix(matrix, target):
    return shortest_path(matrix, (0,0), target)

if __name__ == '__main__':    
    matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
        ]
    
    target = 69
    res = searchMatrix(matrix, target)
    print(res)

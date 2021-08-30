
def searchMatrix(matrix, target) -> bool:
    from_row = 0
    to_row = len(matrix[0])
    from_col = 0
    to_col = len(matrix)

    return sub_matrix(matrix, from_row, to_row, from_col, to_col, target)

def sub_matrix(matrix, from_row, to_row, from_col, to_col, target):
    i = from_row + (from_row + to_row) //2
    j = from_col + (from_col + to_col) // 2

    if matrix[i][j] == target:
        return True
    else:
        pass


if __name__ == '__main__':    
    matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
    ]
    
    target = 30
    res = searchMatrix(matrix, target)
    print(res)






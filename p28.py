import numpy as np
        
    
def spiral_matrix(n: int, clockwise:bool=True) -> np.ndarray:
    """
    create an n by n spiral matrix with 1 at the center 
    then moving to the right in a clockwise direction.
    
    Args:
        n: size of the matrix (odd integer number)
        clockwise:  spiral direction
    """
    
    def right(cell):
        return (cell[0], cell[1] + 1)
    
    def left(cell):
        return (cell[0], cell[1] - 1)
        
    def down(cell):
        return (cell[0] + 1, cell[1])
        
    def up(cell):
        return (cell[0] - 1, cell[1])
    
    if n % 2 == 0:
        raise ValueError("This function only works for odd values of n")
    
    if clockwise:
        dirs = [right, down, left, up]
    else:
        dirs = [left, up, right, down]
    
    mat = np.zeros((n, n))
    cell = (n//2, n//2)
    i = 1
    sprial_number = 1
    mat[cell] = i
    
    # while there are cells equal to 0
    while not mat.all():
        north_west = int((1 + 2 * sprial_number) ** 2)
        
        # first step to enter the new spiral
        cell = dirs[0](cell)
        i += 1
        mat[cell] = i 
        
        snw = int(np.sqrt(north_west)) - 1
        
        for j in range(i+1, i+snw):
            cell = dirs[1](cell)
            i = j
            mat[cell] = i
            
        for j in range(i+1, i+snw+1):
            cell = dirs[2](cell)
            i = j
            mat[cell] = i
        
        for j in range(i+1, i+snw+1):
            cell = dirs[3](cell)
            i = j
            mat[cell] = i
            
        for j in range(i+1, i+snw+1):
            cell = dirs[0](cell)
            i = j
            mat[cell] = i
        
        sprial_number += 1
        
    return mat


def sum_diagonals(mat):
    """ returns the sum of the diagonals of the matrix """
    
    n = mat.shape[0]
    x, y = np.diag_indices(n)
    main_diagonal = mat[(x, y)]
    anti_diagonal = mat[(x, (n-1) - y)]
    
    # subtracting the center value as it shows up in both diagonals
    return main_diagonal.sum() + anti_diagonal.sum() - mat[(n//2, n//2)]
    

def main():
    
    n = 5
    
    mat = spiral_matrix(n, clockwise=True)
    print(mat)
    print()
    print(int(sum_diagonals(mat)))  # 669171001
    

if __name__ == "__main__":
    main()
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  

        # Loop through rows first, than cols than the 3x3 squares 
        # At each loop make sure we dont see duplicate numbers, if we 
        # do than its not a valid sudoku

        # 1) Loop rows 
        for i in range(9):   
            seen = set()  
            for j in range(9):   
                cell = board[i][j]
                if cell != '.' and cell not in seen:  
                    seen.add(cell) 
                elif cell != '.' and cell in seen: 
                    return False
                    

        # 2) Loop cols   
        for i in range(9):   
            seen = set()  
            for j in range(9):   
                cell = board[j][i]
                if cell != '.' and cell not in seen:  
                    seen.add(cell) 
                elif cell != '.' and cell in seen: 
                    return False

        # 3) Loop squares  
        starts = [(0, 0), (3, 0), (6, 0), (0, 3), (0, 6), (3, 3), (3, 6), (6, 3), (6,6)] 
        for p, q in starts: 
            seen = set()
            for i in range(3):    
                for j in range(3):    
                    cell = board[i + p][j + q] 
                    if cell != '.' and cell not in seen:  
                        seen.add(cell) 
                    elif cell != '.' and cell in seen: 
                        return False  
        
        return True

    # Time Taken: 37:14  
    # Time Complexity: O(1), since alwayse have to iterate through 9x9 grid 3 times in differnt ways 
    # Space Complexity O(1), for the sets defined 

    # Note: This problem is dumb, no thinking involved just tricky loops


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 

        # 1) The first binary search is to find the row that our element can be in  
        # - We look at the range and return if the target can be within range

        # 2) Second binary search is to find the col that our element can be in (ie does it exist) 
        # - This should be a classic binary search on the given row (easy stuff) 


        # 1) 
        def rowBinSearch(low, high): 
            
            mid = low + (high - low) // 2

            if high >= low:    
                if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                    return mid 
                elif target > matrix[mid][-1]: # Search right
                    return rowBinSearch(mid + 1, high) 
                elif target < matrix[mid][0]:
                    return rowBinSearch(low, mid - 1) # Search Left

            return False  
        
        row_idx = rowBinSearch(0, len(matrix) - 1)  

        if row_idx != 0 and row_idx == False: 
            return False

        # 2) 
        arr = matrix[row_idx]    

        def colBinSearch(low, high):  

            mid = low + (high - low) // 2

            if high >= low: 

                if arr[mid] == target: 
                    return True 
                elif target > arr[mid]: # Search right
                    return colBinSearch(mid + 1, high) 
                else: 
                    return colBinSearch(low, mid - 1)  

            return False  

        return colBinSearch(0, len(arr) - 1) 


    # Time Taken: 22:23 
    # Time Complexity: O(log(n)) 
    # Space Complexity: O(1)
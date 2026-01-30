class Solution:
    def search(self, nums: List[int], target: int) -> int: 
#################################################################################################### 
# Recursive Implemetation
#################################################################################################### 

        def binSearch(low, high):   
            
            # Ensure our pointers are valid
            if low <= high: 

                # Compute midpoint
                mid = low + (high - low) // 2

                if nums[mid] == target: # If we found target
                    return mid # return index
             
                elif nums[mid] > target: # If midpoint is less than target (target is to the left)
                    return binSearch(low, mid - 1) 
                else: # midpoint greater than target (target is to the right)
                    return binSearch(mid + 1, high) 
            
            # Element not found
            return -1 
        
        # Recursive call
        return binSearch(0, len(nums) - 1) 

#################################################################################################### 
# Iterative Implemetation
####################################################################################################  
        
        # # Left and Right pointers
        # l = 0 
        # r = len(nums) - 1

        # # While the points are valid 
        # while l <= r:  
            
        #     # Compute new midpoint
        #     mid = (l + r) // 2  

        #     # If we found the target
        #     if nums[mid] == target: 
        #         return mid 

        #     # If we overshot (Search left)
        #     elif nums[mid] > target:
        #         r = mid - 1  
        #     # If we undershot (Search Right)
        #     else: 
        #         l = mid + 1 
        
        # # If we cant find the element 
        # return -1
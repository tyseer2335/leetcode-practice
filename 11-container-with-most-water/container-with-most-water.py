class Solution:
    def maxArea(self, height: List[int]) -> int: 

        # Start pointers at both ends and move them into the middle till the collapse 
        # Greedy approach where we move the pointer with the smaller height up to potentially 
        # fill in with more water. Keep track of max so far each step 
        # This works since we are maximizing the vertical area, and horizontal area, while updating 
        # the max so far as we go, thus we will eventually hit the "true max so far" before pointers overlap

        # Pointers
        l = 0 
        r = len(height) - 1  

        # Final answer
        res = float("-inf")

        # While pointers are valid
        while l < r:  
            # Compute area and update max so far if the area is maximum
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area) 
            
            # If the right height is greater, keep it and check left
            if height[l] < height[r]:  
                l += 1 
            else: 
                # Else the left height is greater or equal so keep it
                r -= 1 

        return res

        # Time taken: 11:45 
        # Time Complexity: O(n) 
        # Space Complexity: O(1)
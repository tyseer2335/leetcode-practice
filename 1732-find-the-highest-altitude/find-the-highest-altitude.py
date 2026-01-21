class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        # Start counter at 0 
        c = 0 

        # Result 
        res = 0

        # Loop through and keep track of max so far  

        for i in range(len(gain)): 

            c += gain[i] 
            res = max(c, res) 

        return res 

    # Time taken: 2:44 
    # Time Complexity O(n) 
    # Space Complexity: O(1)
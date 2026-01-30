import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 

        # Use a list to store the result so it can be modified inside the nested function
        # Initialize with infinity since we want the minimum valid speed
        res = [float("inf")]

        def binSearch(low, high): 
            # Standard binary search condition
            if low <= high: 

                # Calculate the middle speed (candidate eating speed)
                k = low + (high - low) // 2  

                # Calculate total hours needed to eat all piles at speed k
                # math.ceil(x / k) gives hours needed for each pile
                speed = sum(math.ceil(x / k) for x in piles)

                # If Koko can finish within h hours, this speed is valid
                if speed <= h:  
                    # Update result with the smaller valid speed
                    res[0] = min(res[0], k)

                    # Try to find an even smaller valid speed on the left side
                    return binSearch(low, k - 1)
                else: 
                    # If it takes more than h hours, speed is too slow
                    # Search the right side for a larger speed
                    return binSearch(k + 1, high) 
        
        # Start binary search with minimum speed 1 and maximum speed max(piles)
        binSearch(1, max(piles))

        # Return the minimum valid eating speed found
        return res[0]

    # Time Complexity: O(nlog(n)) 
    # Space Complexity: O(1)
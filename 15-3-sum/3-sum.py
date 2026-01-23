class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  

        # Result Array
        res = [] 

        # Sort numbers to use 2 pointers
        nums.sort() 

        # Loop through all numbers with the pointer i
        i = 0
        while i < len(nums) - 1:  

            # Define a l and r pointer to do a '2-sum' on remaining part of array
            l = i + 1 
            r = len(nums) - 1 
            
            # The number we need to make in our 2 sum
            targ = -1 * nums[i]  

            # While we have duplicate ajecent numbers we can keep skipping them 
            # to make our solution faster (we need to to handle edgecase: [0,0,0, .... 0])
            while i < len(nums) - 1 and nums[i] == nums[i + 1]: 
                i += 1

            # Start the 2 sum solution with 2 pointers
            while l < r and l < len(nums) - 1:   

                # Sum we have now
                s = nums[r] + nums[l]   
                
                # A possile answer
                ans = [nums[i], nums[r], nums[l]] 
                
                # If sum is equal to target, than we found a valid solution
                if s == targ:   
                    # Add to solution
                    res.append(ans)   

                    # Now we have to keep looking for another solution, 
                    # Increment both pointrs up and keep searching 
                    # This works since we already found a solution with these 2 pointers, 
                    # so they can no longer be part of a new 'unique' solution
                    r -= 1  
                    l += 1 
                    
                    # Now if l and r are the same beside eachother we can keep skipping them again, 
                    # In our 'next solution', this eliminates duplicates and speeds up algorithm
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                # If sum is too big make it smaller by shifting r down
                elif s > targ: 
                    r -= 1   
                else:  
                    # Likewise shift left up if sum is too small
                    l += 1  

            # Increment i to the next number
            i += 1

        # Return result array
        return res

    # Time Taken: 43:53 
    # Time Complexity: O(nlogn) 
    # Space Complexity: O(1), if we dont count res

    # NOTE The last edgecase of [0,0,0, .... 0] took forever to solve, initially used a set to get rid of duplicates 
    # which was 'good enough', but needed hint to skip over consectuive elements to get it to pass, in the future think 
    # about how we can 'slide the window' over consective elements
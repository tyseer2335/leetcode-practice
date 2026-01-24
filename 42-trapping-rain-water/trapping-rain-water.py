class Solution:
    def trap(self, height: List[int]) -> int: 
######################################################################################################################## 
# My Solution (theres an easier way!)
########################################################################################################################

        # Algorithm: 
        # Partition the array into cases that can be solved with the 'edge_peak_algorithm' 

        # 0) Handle edgecases (not enough blocks to hold water and flat case) 
        if len(height) < 3: 
            return 0    
        if len(set(height)) == 1: # flat
            return 0

        # 1) We can first skip consecutive increasing sequence from the right 
        # and consecutive decreasing sequence from the left  
        
        # Left and right pointers
        l = 0 
        r = len(height) - 1 

        # Skip consecutive decreasing sequence from the left  
        while l < len(height) - 1 and height[l] <= height[l+1]: 
            l += 1
        
        # Skip consecutive increasing sequence from the right
        while r > 0 and height[r] <= height[r-1]: 
            r -= 1 

        # 2 Find out where the peaks are, we will partition the array at the peaks 
        # This is computed by iterating from left to right (not including peaks) 
        # and seeing where we see a greater element than the value at index l 
        # Similarly we iterate backwards from r (not including peaks) looking for a 
        # greater element than the vale at index r, and adding it to revese_peaks 
        # This computes left peaks and right peaks than we merge both skipping duplicates 

        # Compute the peaks right to left
        peak_indexs = [l] 
        ptr = l + 1   
        highest = height[l] 

        # Iterate left to right
        while ptr < r:   
            # If we find a bigger height 
            if height[ptr] >= highest:  
                peak_indexs.append(ptr) # Add its index to peak
                highest = height[ptr] # New highest

            ptr += 1
        
        peak_indexs.append(r) # Last peak index is r

        # Now compute peaks from right to left 
        # NOTE that I missed this case in my initial attempt! (Greedy doesnt work)
        reverse_peaks = [r]
        ptr = r - 1
        highest = height[r] 
        
        # Iterate backwards now (literally the same code as above)
        while ptr > l:
            if height[ptr] >= highest:
                reverse_peaks.append(ptr) # Add its index to peak
                highest = height[ptr] # New highest
            ptr -= 1

        reverse_peaks.append(l) # Last peak index is l, since we went backwards 

        # Merge while skipping duplicates (if we counted the peak twice) 
        # NOTE that I missed this case in my initial attempt! (2 searches introduces this step)

        # Loop through all peaks from right to left and if its not in left to right add them
        for p in reverse_peaks:
            if p not in set(peak_indexs):
                peak_indexs.append(p)  

        # Sort the peaks, since indicies must be in the right order  
        # In the next step
        peak_indexs.sort()

        # 3) Use the peak indexes to partition the array and solve these subproblems 
        # with our  'edge_peak_algorithm' function 

        # Use sliding window to construct each partition using the peak_indexs info
        # index and index - 1 are the 2 partitons we want everything between them
        partitions = [] 
        index = 1
        while index < len(peak_indexs):  
            # The magic happens here copy the middle of the array
            partition = height[peak_indexs[index - 1]:peak_indexs[index] + 1]   
            partitions.append(partition)
            # Slide the window down
            index += 1

        # 4) The magic algorithm, since we know each partition has peaks on end and start  
        # we can take minimum peak and subtract the height in each middle part to get water for 
        # that index, and add all the water sums up since none of them will overflow 
        # (thats why we partitioned) 
        def edge_peak_algorithm(height: List[int], partitions: List[int]) -> int:    

            res = 0 # The total water 

            # Loop through all partitions
            for subproblem in partitions:
                water_counter = 0 # How much water is in this rod / middle part
                minimum = min(subproblem[0], subproblem[-1]) # The smalliest peak
                for i in range(1, len(subproblem) - 1):  # Loop through the middle of the partition
                    res += minimum - subproblem[i] # Compute the water in the rod / middle part 
                        
            return res
        
        # Call the function and return
        return edge_peak_algorithm(height, partitions) 

    # Time Taken: Approx 2.5 hours :(
    # Time Complexity: O(n) the number of peaks is always much smaller than the input size, so sorting is negligible  
    # Space Complexity: O(n) for the partitions 
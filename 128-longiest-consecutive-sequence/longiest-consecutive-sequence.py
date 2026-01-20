class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
################################################################################################# 
# Passing Solution O(n)
#################################################################################################

        # We cant sort due to runtime constraints 
        # Check if element is the start of a sequence using a set
        # If it is the start of a sequence see how long the sequence is  
        # If not skip it 

        seen = set(nums) 
        maxSoFar = float("-inf") 

        # Edgecases 
        if nums == []: 
            return 0

        for i in seen:   
            # IMPORTANT: Looping through the set significantly makes the algorithm faster 
            # It will TLE if we dont do this. This doesent change aymptotic running time 
            # but ensures we dont keep checking duplicates!

            # Number is not in seen so start of a seqeunce 
            if i - 1 not in seen:  
                # How long is the sequence 
                seq_length = 1 
                number = i + 1

                while number in seen: 
                    number += 1  
                    seq_length += 1 
                maxSoFar = max(maxSoFar, seq_length) 

            
        return maxSoFar 

    # Time Complexity: O(n)  
    # Space Complexity: O(n) 
    # Time Taken 17:25

################################################################################################# 
# Failing Solution O(n)
#################################################################################################

    # # Here we loop through the list, instead of the set, although this is still O(n), if we have 
    # # a very long repeated sequence ie long sequence starting in 1 and we have many 1s this case 
    # # leads to TLE, with a set we compute this only once

    #     num_set = set(nums)  
    #     res = 0

    #     for i in range(len(nums)):  
    #         if nums[i] - 1 not in num_set: # Start of a sqequence   
    #             start = nums[i]  
    #             seq_length = 0
    #             while start in num_set:  
    #                 seq_length += 1 
    #                 start += 1 
    #             res = max(res, seq_length) 

    #     return res
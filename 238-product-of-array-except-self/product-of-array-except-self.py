class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Compute the prefix 
        # The ith element repersents the product of the i-1 elements before it

        prefix = [1] # First element is prefix is 1 alwayse

        # Loop through and keep track of prefixes starting at second element
        prod_so_far = 1
        for i in range(1, len(nums)):  
            prod_so_far *= nums[i-1] 
            prefix.append(prod_so_far) 

        # Compute the postfix 
        # The ith element repersents the product of the i-1 elements after it
        # The first index in postfix is the postfix for the last element

        postfix = [1] # Last element is 1 since no elements come after
        
        # Loop through backwards compute the postfix 
        post_so_far = 1
        for i in range(len(nums) - 2, -1, -1): 
            post_so_far *= nums[i+1]  
            postfix.append(post_so_far) 
        
        # Multiply each prefix with its corrisponding postfix 
        # Note that postfix is backwards so we multiply the ith index by the n-ith index
        n = len(nums) - 1
        for i in range(len(prefix)): 
            prefix[i] = postfix[n-i] * prefix[i]

        return prefix

    # Time Taken: 16:38 
    # Time Complexity: O(n) 
    # Space Complexity O(n)
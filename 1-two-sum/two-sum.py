class Solution(object):
    def twoSum(self, nums, target): 
        # We can use a hashmap to store number and index 
        # We can then iterate through all numbers and look for a match in O(1)
        # Since we stored the index we can return this easily once we find match

        hashMap = {} 
        for i in range(len(nums)):  
            # Key = number 
            # Value = index
            hashMap[nums[i]] = i   

        for i in range(len(nums)): 
            t = target - nums[i] # Target to find  
            if t in hashMap and hashMap[t] != i: # If target is in our hashmap and its not itself
                return [i, hashMap[t]] 

        # Time Complexity 
        # O(n) where n is the length of the nums 

        # Space Complexity 
        # O(n) for n elements in the hashmap
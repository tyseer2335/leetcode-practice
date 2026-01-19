class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Define buckets for storing each number in the ith frequency
        buckets = [ [] for _ in range(len(nums) + 1)]
        
        # To keep track of each number and its corrisponding counts
        h_map = {}  

        # The answer we return
        res = []

        # For each number in the array build the hashmap to count them
        for num in nums:  
            if num not in h_map: 
                h_map[num] = 0
            h_map[num] += 1 

        # Use the hashmap to 'bucket sort' 
        
        for num in h_map:  
            # The ith array will store unique numbers  
            # repersenting all elements that have count of i 
            buckets[h_map[num]].append(num) 

        # Pointer at end of the array since we need to pop from back 
        # This is because greatiest counts are at the end
        p = len(buckets) - 1 

        # Pop k times
        for i in range(0, k):  
            # Incase we dont have this count decrement the pointer
            while buckets[p] == []: 
                p -= 1  
            
            # Pop one element off, repersenting the most frequent element 
            # and build result
            n = buckets[p].pop() 
            res.append(n) 
        
        # Return result
        return res

        # Time taken 13:10
        # Time Complexity O(n)
        # Space Complexity O(n) 
        # Where n is number of elements in nums

        
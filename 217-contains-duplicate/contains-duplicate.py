class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:  
        # Use sets since it gets rid of duplicates
        return len(nums) != len(set(nums)) 

    # Time Complexity O(n)
    # Space Complexity O(1) 
    # Where n is number of elements in nums
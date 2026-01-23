class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:  
##############################################################################################################################
# Binary Search O(nlogn)
##############################################################################################################################

        # # Binary Search Algorithm
        # def binSearch(low, high, find): 

        #     while low <= high: 

        #         mid = low + (high - low) // 2 

        #         if numbers[mid] == find: 
        #             return mid
        #         elif  find > numbers[mid]: 
        #             return binSearch(mid + 1, high, find) 
        #         else: 
        #             return binSearch(low, mid - 1, find)  
            
        #     return - 1 # Wont execute since we will alwayse have a solution 
        
        # # Loop through all numbers
        # for i in range(len(numbers)):  

        #     # Number we are looking for 
        #     find = target - numbers[i] 

        #     # Find it's index in the array using binary search
        #     index = binSearch(0, len(numbers) - 1, find) 

        #     # If we see that the indicies sum to target and they are not the same number 
        #     # Note this line will alwayse run since we alwayse have a solution
        #     if numbers[i] + numbers[index] == target and i != index:  

        #         # Return the result sorted
        #         res = [i + 1, index + 1] 
        #         res.sort()
        #         return res 

# Time taken 22:02  
# Time Complexity O(nlogn) 
# Space Complexity O(1)

##############################################################################################################################
# 2 Pointer O(n)
############################################################################################################################## 

        # Pointer at start and end
        l = 0 
        r = len(numbers) - 1

        # While sum does not equal target
        curr_sum = numbers[l] + numbers[r] 
        while curr_sum != target: 
            
            # If current sum is too big, move right pointer down, this makes sum smaller 
            # since the array is sorted
            if curr_sum > target:  
                r -= 1 
            else:  
                # If current sum is too small more left up, this makes sum larger since 
                # the array is sorted
                l += 1  

            # Update sum after pointer shifting
            curr_sum = numbers[l] + numbers[r]  

        # Return indicies
        return [l+1,r+1]

    # NOTE: Originally came up with Binary Search Solution    
    # Time Complexity O(n) 
    # Space Complexity O(1)
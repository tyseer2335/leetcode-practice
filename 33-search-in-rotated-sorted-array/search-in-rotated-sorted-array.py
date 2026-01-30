class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Store the first and last elements of the array.
        # These help us determine which sorted portion we are in 

        BOT = nums[0] # Beginning Of array
        TOP = nums[-1] # End Of array

        # Recursive binary search helper
        def binSearch(low, high):

            # Base condition: valid search range
            if low <= high:

                # Calculate middle index
                mid = low + (high - low) // 2

                # If middle element is the target, return its index
                if nums[mid] == target:
                    return mid

                # -------------------------------
                # Case 1: We are in the LEFT sorted portion
                # (values are increasing from BOT to nums[mid])
                # -------------------------------
                if nums[mid] >= BOT:

                    # If target is greater than mid value
                    # OR target is smaller than the smallest value (BOT),
                    # then it must be in the RIGHT half
                    if target > nums[mid] or target < BOT:
                        return binSearch(mid + 1, high)

                    # Otherwise, target lies in the LEFT half
                    else:
                        return binSearch(low, mid - 1)

                # -------------------------------
                # Case 2: We are in the RIGHT sorted portion
                # (values are increasing from nums[mid] to TOP)
                # -------------------------------
                else:

                    # If target is smaller than mid value
                    # OR target is larger than the largest value (TOP),
                    # then it must be in the LEFT half
                    if target < nums[mid] or target > TOP:
                        return binSearch(low, mid - 1)

                    # Otherwise, target lies in the RIGHT half
                    else:
                        return binSearch(mid + 1, high)

            # If the search range is invalid, target was not found
            return -1

        # Start binary search on the entire array
        return binSearch(0, len(nums) - 1) 

    # Time Taken: N/A 
    # Time Complexity: O(nlog(n))

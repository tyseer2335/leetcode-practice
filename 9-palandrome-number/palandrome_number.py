class Solution:
    def isPalindrome(self, x: int) -> bool: 

        # Number (x) as a string
        stringify = str(x) 
        stringify_reversed = stringify[::-1]

        # Return true if the reverse equals the same thing
        return stringify == stringify_reversed
        
# Time Taken: 1:47 
# Time Complexity: O(n) 
# Space Complexity: O(n)
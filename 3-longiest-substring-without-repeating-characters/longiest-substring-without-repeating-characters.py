class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 

        l = 0 
        r = 0  
        res = float("-inf")

        seen = set()    


        while r < len(s): 

            # If we have duplicates we need to shrink 
            while s[r] in seen:
                seen.remove(s[l]) 
                l+=1

            # If we dont we can expand 
            seen.add(s[r]) 
            res = max(res, r - l + 1)
            r += 1

        # return the result 

        return res

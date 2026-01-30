class TimeMap:

    def __init__(self): 
        self.time_store_obj = {}  # {key: [("value", timestamp)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key does not exist, initialize it with the value and timestamp
        if key not in self.time_store_obj:
            self.time_store_obj[key] = [(value, timestamp)]
        # If the key exists, append the value and timestamp to its list
        else:
            self.time_store_obj[key].append((value, timestamp))  

    def get(self, key: str, timestamp: int) -> str: 
        # If the key does not exist, return an empty string
        if key not in self.time_store_obj:
            return ""

        # Define the range to search
        search_range = self.time_store_obj[key]  

        # Find the index of the element we are looking for using binary search
        index = self.binSearch(search_range, 0, len(search_range) - 1, timestamp) 

        # Lookup the value at the found index
        if index == -1: 
            return "" 
        else:
            return search_range[index][0]

    def binSearch(self, search_range, low, high, target): 
        if high >= low: 
            mid = low + (high - low) // 2 

            if search_range[mid][1] == target: 
                return mid 
            elif search_range[mid][1] > target:  # Overshot
                return self.binSearch(search_range, low, mid - 1, target) 
            else:  # Undershot
                return self.binSearch(search_range, mid + 1, high, target)  
        else:   
            # KEY IDEA:
            # Now the high pointer is at the largest valid timestamp <= target.
            # If high < 0, there is no valid timestamp in the range, so return -1 to signal this. 

            # https://ibb.co/MytYpG2c  
            # https://i.ibb.co/7xZwVRYn/Screenshot-2025-11-27-204338.png

            if high < 0: 
                return -1 
            else: 
                return high

# Running Time:
# set(): O(1)
# get(): O(log n)

# Space Complexity:
# O(n)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

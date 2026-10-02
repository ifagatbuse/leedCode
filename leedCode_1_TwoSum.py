class Solution:
    def twosum(self, nums: list[int], target : int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num]= i 
### Hashmap: A structure that stored key-value pairs.
### Dictionary: Python's built-in data structure that implements a hashmap.


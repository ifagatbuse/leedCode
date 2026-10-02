class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


### Hashset: A structure that stores unique elements and allows for fast membership testing.
### Set : Python's built-in data structure that implements a hashset.
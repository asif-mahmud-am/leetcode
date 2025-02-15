# Leetcode 1 #using hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target

        values = {}
        for id, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], id]
            else:
                values[value] = id

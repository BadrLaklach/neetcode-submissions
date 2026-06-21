class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # key: number, value: index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]  # found the pair
            hash_map[num] = i  # store the current number and its index

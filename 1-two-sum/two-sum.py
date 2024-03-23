class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_index_map = {}  # Dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], i]  # Return the indices of the two numbers
            num_index_map[num] = i  # Store t
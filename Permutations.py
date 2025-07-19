from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path: List[int], used: List[bool]):
            if len(path) == len(nums):
                result.append(path[:])  # Add a copy of the current path
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()       # Undo the move
                    used[i] = False  # Mark the number as unused

        backtrack([], [False] * len(nums))
        return result

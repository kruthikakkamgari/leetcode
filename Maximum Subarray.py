class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxSum=float("-inf")
        currentSum=0
        for i in nums:
            currentSum+=i
            maxSum=max(maxSum,currentSum)
            if currentSum<0:
                currentSum=0
        return maxSum

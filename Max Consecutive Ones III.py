class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        right=0
        max_len=0
        count_zeros=0
        while(right<n):
            if  nums[right]==0:
                count_zeros+=1
            if count_zeros>k:
                while  count_zeros>k:
                    if nums[left]==0:
                        count_zeros-=1
                    left+=1
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len
        

class Solution:
    def generate(self,ind,curr,ans,nums):
        if (ind==len(nums)):
            ans.append(curr.copy())
            return
        curr.append(nums[ind])
        self.generate(ind+1,curr,ans,nums)
        curr.pop()
        self.generate(ind+1,curr,ans,nums)                   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ind=0
        curr=[]
        ans=[]
        self.generate(ind,curr,ans,nums)
        return ans

       

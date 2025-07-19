class Solution:
    def generate(self,ind,curr,ans,candidates,target):
        if target==0:
            ans.append(curr.copy())
            return
        if target<0:
            return
        if ind==len(candidates):
            return
        curr.append(candidates[ind])
        self.generate(ind+1,curr,ans,candidates,target-candidates[ind])
        curr.pop()
        for i in range(ind+1,len(candidates)):
            if (candidates[ind]!=candidates[i]):
                self.generate(i,curr,ans,candidates,target)
                break
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ind=0
        curr=[]
        ans=[]
        self.generate(ind,curr,ans,candidates,target)
        return ans

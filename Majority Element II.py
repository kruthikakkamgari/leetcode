class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for key,values in d.items():
            if values>n//3:
                l.append(key)
        return l
        


        

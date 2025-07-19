class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        left=0
        right=0
        maxLen=0
        d={}
        while(right<n):
            if fruits[right] in  d:
                d[fruits[right]]+=1
            else:
                d[fruits[right]]=1
            if len(d)>2:
                while len(d)>2:
                    d[fruits[left]]-=1
                    if d[fruits[left]]==0:
                        del d[fruits[left]]
                    left+=1
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen
        

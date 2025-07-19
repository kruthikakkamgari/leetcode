class Solution:
    def generate(self,ind,curr_str,ans,o,c,n):
        if o==c and ind==2*n:
            ans.append(curr_str)
            return
        if o>n:
            return
        self.generate(ind+1,curr_str+"(",ans,o+1,c,n)
        if o>c:
            self.generate(ind+1,curr_str+")",ans,o,c+1,n)
    def generateParenthesis(self, n: int) -> List[str]:
        ind=0
        curr_str=""
        ans=[]
        o=0
        c=0
        self.generate(ind,curr_str,ans,o,c,n)
        return ans
        

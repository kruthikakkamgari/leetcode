class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftMax=[-1]*n
        leftMax[0]=height[0]
        for i in range(1,n):
            leftMax[i]=max(height[i],leftMax[i-1])
        rightMax=[-1]*n
        rightMax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(height[i],rightMax[i+1])
        MinArray=[]
        for i in range(0,n):
            MinArray.append(min(rightMax[i],leftMax[i]))
        result=0
        for i in range(0,n):
            result+=MinArray[i]-height[i]
        return result

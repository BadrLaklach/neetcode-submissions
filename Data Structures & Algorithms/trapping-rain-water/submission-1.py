class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        res= 0 
        l,r=0,len(height)-1
        MaxLeft , MaxRight = height[l],height[r]

        while l < r:
            if MaxLeft < MaxRight:
                l+=1
                MaxLeft = max(MaxLeft,height[l])
                res += MaxLeft - height[l]

            else:
                r-=1
                MaxRight = max(MaxRight,height[r])
                res += MaxRight - height[r]
        
        return res

        
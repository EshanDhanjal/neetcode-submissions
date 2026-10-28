class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = (right-left)*(min(heights[left],heights[right]))

        while left < right:
            width = right-left
            height = min(heights[left],heights[right])
            a = width*height
            res = max(res, a)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left+=1
        return res
            


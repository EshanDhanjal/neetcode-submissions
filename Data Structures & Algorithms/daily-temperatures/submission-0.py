class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                sT, sInd = stack.pop()
                res[sInd] = (i-sInd)
            stack.append([j,i])
        return res
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        big = 0
        for rec in rectangles:
            leng = min(rec[0], rec[1])
            if leng > big:
                res = 1
                big = leng
            elif leng == big:
                res += 1
        return res
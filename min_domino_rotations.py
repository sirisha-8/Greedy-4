#Time Complexity : O(n), where n is  len of tops/botoms array
#Space Complexity : O(1)

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops)==0:
            return -1
        n = len(tops)
        num = tops[0]
        self.maxf = float('inf')
        
        def count_min(num):
            top_c = 0
            bottom_c = 0
            for i in range(0,n):
                t = tops[i]
                b = bottoms[i]
                if  t != num and b != num:
                    return -1
                elif num == t and num != b:
                    bottom_c+=1
                elif num != t and num == b:
                    top_c+=1
                else:
                    pass

            self.maxf = min(self.maxf,min(top_c,bottom_c))
            return 0     
                
        if count_min(num) != -1:
            return self.maxf
        else:
            self.maxf = float('inf')
            if count_min(bottoms[0]) != -1:
                return self.maxf
            else:
                return -1
        
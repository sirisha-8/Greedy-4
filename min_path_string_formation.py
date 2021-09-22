#Time Complexity : O(mn), where m is len of source, n is len of target
#Space Complexity : O(1)

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if len(source) ==0 or not source :
            return -1
        if len(target)==0 and  len(source)==0:
            return 0
        if source==target:
            return 1
        
        result = 1
        si = 0
        ti = 0
        sn = len(source)
        tn = len(target)
        sourceset = set()
        for item in source:
            sourceset.add(item)
            
        
        while(ti<tn):
            tc = target[ti]
            if tc not in sourceset:
                return -1
            while si<sn and source[si]!=tc:  #make two pointers point to same index
                si+=1
            if si==sn:  #if out of bounds that means we used input string 1 time then reset index=0
                result+=1
                si = 0
            else:  #if characters are matching, then increment both pointers
                si+=1
                ti+=1
        return result
            
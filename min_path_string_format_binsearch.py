#Time Complexity : O(m+n), where m is len of source, n is len of target
#Space Complexity : O(1)
from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if len(source) ==0 or not source :
            return -1
        if len(target)==0 and  len(source)==0:
            return 0
        if source==target:
            return 1
        
        result = 1
        si = ti = 0
  
        sn = len(source)
        tn = len(target)
        hashmap = defaultdict(list)
        for index,item in enumerate(source):
            hashmap[item].append(index)
            
        def binsearch(arr,target):
            low = 0
            high = len(arr)-1
            while(low<=high):
                mid = low+(high-low)//2
                if arr[mid]==target:
                    return mid
                elif target < arr[mid]:
                    high = mid-1
                else:
                    low = mid+1
            return low

        
        while(ti <tn):
            tc = target[ti]
            if tc not in hashmap:
                return -1
            index = binsearch(hashmap[tc],si)
           
            if index == len(hashmap[tc]):
                #if didnt find index close to target that means ts before target so we completed 1 iteration
                si = 0
                result+=1
           
            else:
                ti+=1
                si= hashmap[tc][index]+1
                
        return result
            
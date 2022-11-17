class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])
        #print(intervals)
        new=[]
        start,end=intervals[0][0],intervals[0][1]
        
        for i in intervals:
            #print(new)
            #print("yo",start,end)
            
            curstart,curend=i[0],i[1]
     
            if curstart <= end:
                end=max(end,curend)
            else:
                new.append([start,end])
                start=curstart
                end=curend
                
        new.append([start,end])
        return new
            
            
            
        
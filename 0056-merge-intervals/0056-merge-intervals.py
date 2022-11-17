class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])
        # compare check and check + 1, until check == len(intervals)
        check = 0
        while check < len(intervals)-1:
            nx = intervals[check+1]
            cu = intervals[check]
            if nx[0] <= cu[1] and nx[0] >= cu[0]:
                cu[1] = max(cu[1], nx[1])
                intervals.pop(check+1)
            else:
                check+=1

        return intervals
            
            
        
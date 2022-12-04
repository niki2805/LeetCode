class Solution:
    def frequencySort(self, s: str) -> str:
        
        res=[]
        freq=Counter(s)
        heap=[]
        for k,v in freq.items():
            heap.append((-v,k))
            
        heapq.heapify(heap)
        
        while heap:
            w=heapq.heappop(heap)
            res.append(w[1]* -w[0])
            
        return "".join(res)
        
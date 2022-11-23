class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row=defaultdict(set)
        col=defaultdict(set)
        grid=defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board)):
                cur=board[i][j]
                
                if cur=='.':
                    continue
                
                if cur in row[i] or cur in col[j] or cur in grid[(i//3,j//3)]:
                    return False
                
                row[i].add(cur)
                col[j].add(cur)
                grid[(i//3,j//3)].add(cur)
                
        return True
            
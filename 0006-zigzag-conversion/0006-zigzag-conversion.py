class Solution:
    def convert(self, s: str, numRows: int) -> str:
       
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        print(result)
        index, direction = 0, 1

        for char in s:
            #print(char)
            #print(index)
            result[index] += char
            if index == 0:
                direction = 1
            elif index == numRows -1:
                direction = -1
                
            index += direction

        return ''.join(result)
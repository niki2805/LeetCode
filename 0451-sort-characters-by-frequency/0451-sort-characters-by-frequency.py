class Solution:
    def frequencySort(self, s: str) -> str:
        res = ''
        d = {l: c for l, c in sorted(Counter(s).items(), key=lambda i: i[1], reverse=True)}
        for l in d:
            res += l*d[l]
        return res
        
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_s = s + s 
        index_in_double_s = double_s.index(s, 1)
        return index_in_double_s < len(s)

sol = Solution()

result = sol.repeatedSubstringPattern("abab")
print(result)

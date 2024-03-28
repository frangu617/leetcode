class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # Subtract 1 at the end because left and right are beyond the palindrome boundaries

        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)  # Check for odd-length palindromes
            len2 = expandAroundCenter(i, i + 1)  # Check for even-length palindromes

            # Use the longer one
            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

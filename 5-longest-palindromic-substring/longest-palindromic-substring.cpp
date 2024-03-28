#include <string>
using std::string;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        if (s.size() == 1) return s;

        int start = 0, end = 0;

        for (int i = 0; i < s.size(); i++) {
            // Check for odd-length palindromes
            int len1 = expandAroundCenter(s, i, i);
            // Check for even-length palindromes
            int len2 = expandAroundCenter(s, i, i + 1);

            // Find the longest of the two
            int len = std::max(len1, len2);

            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        return s.substr(start, end - start + 1);
    }

private:
    int expandAroundCenter(const string& s, int left, int right) {
        while (left >= 0 && right < s.size() && s[left] == s[right]) {
            left--;
            right++;
        }
        // Subtract 1 at the end because when the while loop exits,
        // left and right are one step beyond the palindrome boundaries
        return right - left - 1;
    }
};

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Set to store characters in the current substring
        max_length = 0     # Variable to store the length of the longest substring
        start_index = 0    # Variable to store the start index of the current substring

        for end_index, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[start_index])  # Remove characters from the set until no duplicates are found
                start_index += 1
            char_set.add(char)  # Add the current character to the set
            max_length = max(max_length, end_index - start_index + 1)

        return max_length
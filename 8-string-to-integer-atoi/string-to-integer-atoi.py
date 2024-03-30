class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespace
        s = s.lstrip()

        # Check if string is empty after removing whitespace
        if not s:
            return 0

        # Determine sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Read digits until a non-digit character is encountered
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Apply sign
        result *= sign

        # Clamp to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
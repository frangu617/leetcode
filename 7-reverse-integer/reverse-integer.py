class Solution:
    def reverse(self, x: int) -> int:
        # Check if x is negative
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        # Convert integer to string, reverse it, and convert back to integer
        reversed_str = str(x)[::-1]
        reversed_int = int(reversed_str) * sign

        # Check if reversed integer is within the 32-bit signed integer range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        else:
            return reversed_int
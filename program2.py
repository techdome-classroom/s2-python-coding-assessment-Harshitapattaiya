class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        t= 0
        p = 0

        for char in reversed(s):
            current_value = roman_map[char]

            if current_value < p:
                t -= current_value
            else:
                t += current_value

            p = current_value
        
        return t




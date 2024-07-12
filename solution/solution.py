class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # If x is less than y, swap their values and swap the roles of 'a' and 'b'
        if x < y:
            x, y = y, x
            a, b = 'b', 'a'
        else:
            a, b = 'a', 'b'

        total = 0
        dxy = x - y
        ab_count = a_count = b_count = 0

        # Iterate over the string
        for char in s:
            # If the character is not 'a' or 'b', process the current counts
            if char not in 'ab':
                if b_count > a_count:
                    a_count, b_count = b_count, a_count
                if a_count > 0:
                    total += ab_count * dxy + b_count * y
                    ab_count = a_count = b_count = 0
            # If the character is 'a', increment the count of 'a'
            elif char == a:
                a_count += 1
            # If the character is 'b', increment the count of 'b' and form 'ab' if possible
            else:
                b_count += 1
                if a_count > ab_count:
                    ab_count += 1

        # Process the remaining counts
        total += ab_count * dxy + min(a_count, b_count) * y

        return total
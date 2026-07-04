class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0

        while i < len(chars):

            j = i

            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            # Write the character
            chars[write] = chars[i]
            write += 1

            count = j - i

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            i = j

        return write
            
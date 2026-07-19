class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        
        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
            
        num = abs(numerator)
        den = abs(denominator)
        
        # Integral part
        res.append(str(num // den))
        num %= den
        
        if num == 0:
            return "".join(res)
            
        res.append(".")
        
        # Store fractional part digits in a separate list
        fraction_digits = []
        remainder_map = {}
        
        while num != 0:
            if num in remainder_map:
                # Get the index where the repetition starts
                repeat_start = remainder_map[num]
                
                # Split the fractional part and wrap the repeating block in parentheses
                non_repeating = "".join(fraction_digits[:repeat_start])
                repeating = "".join(fraction_digits[repeat_start:])
                
                return "".join(res) + non_repeating + "(" + repeating + ")"
                
            remainder_map[num] = len(fraction_digits)
            
            num *= 10
            fraction_digits.append(str(num // den))
            num %= den
            
        return "".join(res) + "".join(fraction_digits)
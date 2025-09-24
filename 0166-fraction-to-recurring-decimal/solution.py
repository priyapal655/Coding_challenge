class Solution(object):
    def fractionToDecimal(self, numerator, denominator):

        if numerator == 0:
            return "0"
            
        result = []
        if (numerator < 0) != (denominator < 0):
            result.append("-")
        
        # Make both positive
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        numerator %= denominator
        
        if numerator == 0:  # No fractional part
            return "".join(result)
        
        # Fractional part
        result.append(".")
        remainder_map = {}  # Maps remainder -> position in result
        
        while numerator != 0:
            if numerator in remainder_map:
                # Found repeating cycle
                index = remainder_map[numerator]
                result.insert(index, "(")
                result.append(")")
                break
            
            # Record remainder and its position
            remainder_map[numerator] = len(result)
            
            # Long division step
            numerator *= 10
            result.append(str(numerator // denominator))
            numerator %= denominator
        
        return "".join(result)

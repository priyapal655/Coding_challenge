class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        i = len(a)-1
        j=  len(b)-1
        carry =0

        while i>=0 or j>=0 or carry:
            if(i>=0):
                carry += int(a[i])
                i-=1
            if(j>=0):
                carry += int(b[j])
                j-=1
            
            result= str(carry%2) + result
            carry //=2
        return result

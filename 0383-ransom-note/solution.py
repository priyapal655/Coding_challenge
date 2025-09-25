class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazineDict = {}

        for char in magazine:
            if(char in magazineDict):
                 magazineDict[char] +=1
            else:
                magazineDict[char]= 1
        
        for char in ransomNote:
            if (char in magazine and magazineDict[char]>0):
                magazineDict[char]-=1
            else:
                return False       

        return True 
        

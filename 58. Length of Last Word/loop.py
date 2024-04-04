def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s[::-1]
        while(s[0] == ' '):
            s = s.replace(' ','',1)
        s = s.split(' ') 
        return s[0][::-1]
        

print(lengthOfLastWord("Kashvi Gandhi   "))


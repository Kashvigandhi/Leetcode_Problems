# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        left = 0
        right = len(s) - 1
        while left <= right:
                while left <= right and (s[left] not in vowels or s[right] not in vowels):
                        if s[left] not in vowels:
                                left += 1
                        if s[right] not in vowels:
                                right -= 1
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        return "".join(s)
print(reverseVowels("leetcode"))

                
        
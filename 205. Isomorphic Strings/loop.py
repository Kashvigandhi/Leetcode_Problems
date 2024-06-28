# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
#zip only runs till length of shorter list. Zip is faster than enumerate
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t): return False
    letterMap = {}
    for x,y in zip(s,t):
        if x in letterMap:
            if letterMap[x] != y:
                return False
        else:
            if y in letterMap.values() : return False
            letterMap[x] = y
    return True

print(isIsomorphic("",""))
        



        
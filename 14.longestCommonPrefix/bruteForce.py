# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    for index,letter in enumerate(strs[0]):
        for word in strs:
            if index >= len(word) or word[index] != letter:
                return prefix
        prefix = prefix + letter
    return prefix



print(longestCommonPrefix(["flower","flow","flight"]))
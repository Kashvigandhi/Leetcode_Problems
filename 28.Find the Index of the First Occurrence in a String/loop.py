# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# first we check if length of needle is more than length of haystack and return -1 one if it is.
# if above condition is not true we check if the lengths are equal. if yes, then we return 0(index of first char) if strings are equal, else -1
# if none of the conditions above is true, i.e, len of needle is less than len of haystack, then we create an outer loop that runs from first index
# of haystack till len of needle + 1. This is because we don't need to go any further since then the substring of haystack from i till end will be
# less than needle. we have already initialised firstOccurence with -1. we check in each iteration of outer loop if that character of haystack is eqaul
# to first character of needle. if yes,then we change the value of firstOccurence to that index and check for the equality of subsequent characters
# using an inner loop. If we find an inequality, we reset firstOccurence to -1 and break out of the inner loop. 
# If, however, we find that all characters are equal, we return firstOccurence as the job is done. This also prevents value of firstOccurence
# being overwritten if another match is found.
def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(len(haystack) < len(needle)):
            return -1
        if(len(haystack) == len(needle)):
            return 0 if haystack == needle else -1
        firstOccurence = -1
        for i in range(len(haystack) - len(needle)+1):
            if(haystack[i] == needle[0]):
                firstOccurence = i
                for j in range(1,len(needle)):
                    i += 1
                    if(haystack[i] != needle[j]):
                        firstOccurence = -1
                        break
                if firstOccurence != -1:
                    return firstOccurence
        return firstOccurence
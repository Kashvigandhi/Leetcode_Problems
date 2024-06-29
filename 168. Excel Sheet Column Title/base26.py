# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#Both complexity : O(log(columnNumber))
def convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    title = ""
    while columnNumber > 0:
        columnNumber = columnNumber - 1
        remainder = columnNumber % 26
        title += (chr(ord('A') + remainder))
        columnNumber = (columnNumber // 26) 
    return title[::-1]

print(convertToTitle(701))

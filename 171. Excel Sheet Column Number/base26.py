# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    columnTitle = columnTitle[::-1]
    A = ord('A')
    num = 0
    for index,letter in enumerate(columnTitle):
        num += (ord(letter) - A + 1) * (26 ** index)
    return num
print(titleToNumber('ZY'))

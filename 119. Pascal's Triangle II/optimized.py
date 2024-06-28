# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#Space: O(n^2), Time: O(n^2)
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0 : return [[1]]
    if rowIndex == 1 : return [[1],[1,1]]
    pascal = [[1], [1,1], [1,2,1]]
    i = 2
    while True:
        if i == rowIndex : return pascal[-1]
        pascal.append([1,1])
        for j in range(1,len(pascal[-2])):
            pascal[-1].insert(-1,pascal[-2][j - 1] + pascal[-2][j])
        i += 1


print(getRow(5))







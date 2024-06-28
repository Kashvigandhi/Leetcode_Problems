# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#Space: O(n^2), Time: O(n^2)
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    pascal = [[1]]
    i = 0
    while True:
        if i == rowIndex : return pascal[-1]
        temp = [0] + pascal[-1] + [0]
        res = []
        for j in range(len(temp) - 1):
            res.append(temp[j] + temp[j + 1])
        pascal.append(res)
        i += 1

print(getRow(1))






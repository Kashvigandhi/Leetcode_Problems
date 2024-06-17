# Given an integer numRows, return the first numRows of Pascal's triangle.

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1 : return [[1]]
    if numRows == 2 : return [[1],[1,1]]
    l1 = [[1],[1,1]]
    for i in range(numRows - 2):
        temp = l1[-1]
        temp1 = [temp[0]]
        for j in range(1,len(temp)):
            temp1.append(temp[j - 1] + temp[j])
        temp1.append(temp[-1])
        l1.append(temp1)

    print(l1)

generate(4)




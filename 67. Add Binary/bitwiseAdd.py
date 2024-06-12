# Given two binary strings a and b, return their sum as a binary string.
#Time and Space complexity both O(n)
def addBinary( a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    res = ""
    carry = 0
    a = a[::-1]
    b = b[::-1]
    if(len(a) != len(b)):
        if(len(a) > len(b)):
            for i in range(len(a)-len(b)):
                b += "0"
        else:
            for i in range(len(b)-len(a)):
                a += "0"

    for num1,num2 in zip(a,b):
        num1 = int(num1)
        num2 = int(num2)
        res += str(carry ^ num1 ^ num2)

        carry = 1 if [num1,num2,carry].count(1) >= 2 else 0
    if carry == 1 : res += "1"
    print(res[::-1])
    
        


addBinary("100","11")
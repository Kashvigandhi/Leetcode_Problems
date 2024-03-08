
def isPalindrome(x):
    x = str(x)
    x_arr = list(x)
    pointer1 = 0
    pointer2 = len(x_arr) - 1

    for i in range(len(x_arr)//2):
        x_arr[pointer1],x_arr[pointer2] = x_arr[pointer2],x_arr[pointer1] 
        print(x)
        pointer1 += 1
        pointer2 -= 1
    x_arr = ''.join(x_arr)
    return x_arr == x

print(isPalindrome(10))
def romanToNumbers(s):
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    number = 0
    while(len(s) != 0):
        if(s[:2] in d):
            number += d[s[:2]]
            s = s[2::]
        else:
            number += d[s[:1]]
            s = s[1:]
    print(number)

romanToNumbers('MIV')


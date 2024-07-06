def patternMatch(pattern, s):
    hashset = {}
    s = s.split(" ")
    if len(s) != len(pattern): return False
    for i in range(len(pattern)):
        if pattern[i] in hashset:
            if (hashset[pattern[i]] != s[i]):
                return False
        else:
            if (s[i] in hashset.values()):
                return False
            hashset[pattern[i]] = s[i]

    return True
print(patternMatch("abba","dog cat cat dog"))

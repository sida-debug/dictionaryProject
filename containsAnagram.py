def contains_anagram(s, p):
        d1, d2 = {}, {}
        for ch in s:
            if ch in d1:
                d1[ch] += 1
            else:
                d1[ch] = 1
        for ch in p:
            if ch in d2:
                d2[ch] += 1
            else:
                d2[ch] = 1
        if d1 == d2:
            return True
        else:
            return False

print(contains_anagram("iceman", "cinema"))
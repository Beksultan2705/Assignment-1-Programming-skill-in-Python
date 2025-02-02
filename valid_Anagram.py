def anagram(s: str, t: str):
    return sorted(s) == sorted(t)

s = 'rat'
t = 'car'
print(anagram(s, t))

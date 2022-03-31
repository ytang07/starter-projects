s = "abcdefg"

# any character
print(s[3]) # expect d

# negative indices
print(s[-2]) # expect second to last = f

# slicing positions
print(s[1:4]) # expect 1, 2, 3 = bcd
print(s[:2]) # expect beginning to 1 = ab

#slicing positions _n_ at a time
print(s[0::2]) # expect every 2 from 0 to end = aceg
print(s[0:7:3]) # expect every 3 from 0 to 6 = adg
print(s[5:1:-1]) # expect reverse entries from 5 to 2 = fedc
print(s[-2:-5:-2]) # expect reverse every other entry from second to fifth to last = fd

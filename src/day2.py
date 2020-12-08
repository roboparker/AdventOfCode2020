import re
from operator import xor

def getOldPasswordValidityCounts():
    invalid = 0
    valid = 0
    input = open('input/day2.txt', 'r')
    for line in input:
        parts = re.split("[\-\s\:]", line)
        min = int(parts[0])
        max = int(parts[1])
        needle = parts[2]
        heystack = parts[4]
        count = len(re.findall(needle, heystack))
        if count > max or count < min:
            invalid += 1
        else:
            valid += 1
    input.close()
    return valid, invalid

def getPasswordValidityCounts():
    invalid = 0
    valid = 0
    input = open('input/day2.txt', 'r')
    for line in input:
        parts = re.split("[\-\s\:]", line)
        pos1 = int(parts[0])-1
        pos2 = int(parts[1])-1
        needle = parts[2]
        heystack = parts[4]
        if xor(heystack[pos1] == needle, heystack[pos2] == needle):
            valid += 1
        else:
            invalid += 1
    input.close()
    return valid, invalid


print("Day 2, Challenge 1")
valid, invalid = getOldPasswordValidityCounts()
print(valid, " valid password(s) and", invalid, "invalid password(s)")

print("Day 2, Challenge 2")
valid, invalid = getPasswordValidityCounts()
print(valid, " valid password(s) and", invalid, "invalid password(s)")
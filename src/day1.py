def getSet():
    input = open('input/day1.txt', 'r')
    set = []
    for num in input:
        set.append(int(num))
    input.close()
    set.sort()
    return set


def getSubsetSum2(set, n, sum):
    l = 0
    r = n - 1
    while l < r:
        total = set[l] + set[r]
        if total == sum:
            return True, set[l], set[r]
        elif total < sum:
            l += 1
        else:
            r -= 1
    return False, 0, 0

def getSubsetSum3(set, n, sum):
    for i in range(0, n - 2):
        l = i + 1
        r = n - 1
        while (l < r):
            total = set[i] + set[l] + set[r]
            if total == sum:
                return True, set[i], set[l], set[r]
            elif total < sum:
                l += 1
            else:
                r -= 1
    return False, 0, 0, 0

sum = 2020
set = getSet()
length = len(set)

print("Day 1, Challenge 1")
result, a, b = getSubsetSum2(set, length, sum)
if result:
    print("subset found", a, b, a*b)
else:
    print("subset not found")

print("Day 1, Challenge 2")
result, a, b, c = getSubsetSum3(set, length, sum)
if result:
    print("subset found", a, b, c, a*b*c)
else:
    print("subset not found")

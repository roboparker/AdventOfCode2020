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

def challenge_1_1():
    sum = 2020
    set = getSet()
    length = len(set)
    result, a, b = getSubsetSum2(set, length, sum)
    if result:
        print("Subset found", a, b)
        print("Product", a * b)
    else:
        print("Subset not found")

def challenge_1_2():
    sum = 2020
    set = getSet()
    length = len(set)
    result, a, b, c = getSubsetSum3(set, length, sum)
    if result:
        print("Subset found", a, b, c)
        print("Product", a * b * c)
    else:
        print("Subset not found")
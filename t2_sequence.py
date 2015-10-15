
def position(number, n):
    res = (number - 10**(n - 1)) * n + 1
    n = n - 1
    while n > 0:
        res = res + (10**(n) - 10**(n - 1)) * n
        n = n - 1
    return res

def generate(a, lenA, n, shift):
    if shift == 0:
        g = a[0:n]
        if g[0] == '0':
            return False, ''
        return True, g

    nextStr = ''
    if shift + n <= lenA:
        nextStr = a[shift:shift + n]
    else:
        nextStr = a[shift:]
        if nextStr[0] == '0':
            return False, ''

        last = int('1' + a[:shift]) + 1
        lastStr = str(last)
        nextStr = nextStr + lastStr[1:]
    if nextStr[0] == '0':
        return False, ''
    prevInt = int(nextStr) - 1
    prevStr = str(prevInt)
    pos = n - shift
    k = 0
    while pos < n:
        if prevStr[pos] != a[k]:
            return False, ''
        k = k + 1
        pos = pos + 1
    return True, prevStr

def check(a, lenA, n, prevMin):
    success = False
    shift = 0
    delta = 0
    start = prevMin
    currPos = 0
    while shift != n:
        succ, gen = generate(a, lenA, n, shift)
        if not succ:
            shift = shift + 1
            continue
        start = int(gen)
        if start >= prevMin:
            shift = shift + 1
            continue
        diff = False
        currPos = shift + n
        if currPos >= lenA or len(gen) == lenA:
            if start < prevMin:
                prevMin = start
                success = True
                if shift > 0:
                    delta = n - shift
            shift = shift + 1
            continue

        while currPos != lenA:
            genInt = int(gen)
            if shift == 0:
                genNext = genInt + 1
            else:
                genNext = genInt + 2
            gen = str(genNext)
            lenGen = len(gen)
            i = 0
            while i < lenGen and currPos < lenA:
                if a[currPos] != gen[i]:
                    diff = True
                    break
                currPos = currPos + 1
                i = i + 1

            if diff:
                shift = shift + 1
                break
            if currPos == lenA:
                if start < prevMin:
                    prevMin = start
                    success = True
                    if shift > 0:
                        delta = n - shift
                shift = shift + 1
    return success, prevMin, delta


def firstOccurrence(a, prevMin):
    if int(a) == 0:
        start = '1' + a
        n = len(start)
        return position(int(start), n) + 1
    n = 1
    lenA = len(a)
    while n <= lenA:
        success, start, delta = check(a, lenA, n, prevMin)
        if success:
            pos = position(start, n) + delta
            return pos
        n = n + 1
    return position(prevMin, n - 1)

while True:
    try:
        a = raw_input("Enter the number: ")
        if len(a) > 0 and a[0] == '0':
            prevMin = int('1' + a)
        else:
            prevMin = int(a)
        fo = firstOccurrence(a, prevMin)
        print(fo)
    except:
        break



import sys
def findStart_2x2(a, b):
    startA = 0
    endA = len(a)
    startB = 0
    endB = len(b)
    while endA - startA != 2:
        midA = (startA + endA - 1) // 2
        midB = (startB + endB - 1) // 2
        if a[midA] >= b[midB]:
            endA = midA + 1
            startB = midB + (endB - startB + 1) % 2
        else:
            endB = midB + 1
            startA = midA + (endA - startA + 1) % 2
    return startA, startB

def median_2x2(a, startA, b, startB):
    i = startA
    j = startB
    countA = 0
    countB = 0
    c = []
    while countA + countB != 3:
        if(countA < 2) and (countB < 2):
            if a[i] <= b[j]:
                c.append(a[i])
                i = i + 1
                countA = countA + 1
            else:
                c.append(b[j])
                j = j + 1
                countB = countB + 1
        elif (countA < 2):
            c.append(a[i])
            i = i + 1
            countA = countA + 1
        else:
            c.append(b[j])
            j = j + 1
            countB = countB + 1
    return (c[1] + c[2]) / 2.0
            
def findMedian(a, b):
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return (a[0] + b[0]) / 2.0
    else:
        startA, startB = findStart_2x2(a, b)
        return median_2x2(a, startA, b, startB)
    
if len(sys.argv) == 2:
    fileName = sys.argv[1]
else:
    fileName = 'data1.txt'
try:
    f = open(fileName, 'r')
    while True:
        lineA = f.readline().rstrip('\n')
        lineB = f.readline().rstrip('\n')
        if len(lineA) == 0 or len(lineB) == 0:
            break
        a = list(map(int, lineA.split()))
        b = list(map(int, lineB.split()))
        if len(a) != len(b):
            continue
        print(findMedian(a, b))
    f.close()
except IOError:
    a = [1, 2, 3, 4]
    b = [1, 4, 5, 6]
    print(findMedian(a, b))

def getShiftedString(s, leftShifts, rightShifts):
    i = (leftShifts - rightShifts) % len(s)
    return s[i:] + s[:i]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    leftShifts = int(input().strip())

    rightShifts = int(input().strip())

    result = getShiftedString(s, leftShifts, rightShifts)

    fptr.write(result + '\n')

    fptr.close()

#!/usr/bin/env python3
import sys

encodingMap = {
    0: ':SeriousSloth:',
    1: ':panik:'
}

inputString = sys.stdin.read()
decodedString = ''

# empty list to store the decoded bits
bits = []

while True:
    # try to find both symbols in the string
    # the closer one is the bit we are trying to read
    nearest = None
    minDistance = len(inputString)

    for key in encodingMap.keys():
        # search for the value
        distance = inputString.find(encodingMap[key])
        if (distance != -1) and (distance < minDistance):
            minDistance = distance
            nearest = key

    if nearest is None:
        break

    bits.append(nearest)
    newStart = minDistance + len(encodingMap[nearest])
    inputString = inputString[newStart:]

while len(bits) > 8:
    # integer representation of ascii
    asciiNumber = 0
    for i in range(8):
        # set apprpriate bits in final number
        asciiNumber = asciiNumber | (bits.pop(0) << i)

    decodedString += chr(asciiNumber)

print(decodedString)

#!/usr/bin/env python3
import sys

encodingMap = {
    '0': ':SeriousSloth:',
    '1': ':panik:'
}

inputString = sys.stdin.read()
decodedString = ''

# empty string of decoded bits
bits = ''

while True:
    # try to find both symbols in the string
    # the closer one represents the next bit
    nearest = None
    minDistance = len(inputString)

    for key in encodingMap.keys():
        # search for the substring
        distance = inputString.find(encodingMap[key])
        if (distance != -1) and (distance < minDistance):
            minDistance = distance
            nearest = key

    if nearest is None:
        break

    bits += nearest
    newStart = minDistance + len(encodingMap[nearest])
    inputString = inputString[newStart:]

while len(bits) >= 8:
    # read the first 8 characters and convert them into integer
    byte = int(bits[:8], 2)
    # delete the first 8 characters from the string
    bits = bits[8:]
    decodedString += chr(byte)

print(decodedString)

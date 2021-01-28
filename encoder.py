#!/usr/bin/env python3
import sys

# what should be written in output instead of original bytes
encodingMap = {
    '0': ':SeriousSloth:',
    '1': ':panik:'
}
# inbetween the bits
bitSeparator = ' '
# after each byte
byteSeparator = '\n'
# both separators are only cosmetic, decoder ignores them
# make sure, that separators do not contain any string from encodingMap

inputString = sys.stdin.read()
encodedString = ''

for character in inputString:
    # convert every character of the string into an integer
    byte = ord(character)
    # convert the byte into string of 1's and 0's
    binaryString = format(byte, '#010b')
    # remove '0b' prefix
    binaryString  = binaryString[2:]

    for bit in binaryString:
        # write all bits in the final encoded string
        encodedString += encodingMap[bit]
        encodedString += bitSeparator
    # byteSeparator after each character
    encodedString += byteSeparator

print(encodedString)

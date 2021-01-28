#!/usr/bin/env python3

# what should be written in output instead of original bytes
encodingMap = {
    0: ':SeriousSloth:',
    1: ':panik:'
}
# inbetween the bits
bitSeparator = ' '
# after each byte
byteSeparator = '\n'
# both separators are only cosmetic, decoder ignores them
# make sure, that separators do not contain any string from encodingMap

inputString = input()
encodedString = ''

for character in inputString:
    # convert every character of the string into an integer
    num = ord(character)
    # convert the integer into list of corresponding bits
    for i in range(8)
        # shift the bit in place of 1's
        bit = (num >> i) & 1
        # result is already 0 or 1
        # convert into fila string
        encodedString += outputMap[bit] + bitSeparator

    encodedString += byteSeparator

print(encodedString)

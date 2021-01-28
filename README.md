# string2bits
 Converts ASCII string into discrete bits, which can be represented with emotes.
 
## Usage
Both scripts use stdin and stdout files. That means, that you can use pipes to get data in and out.
```
echo 'hello' | ./encoder.py
```

You can use input and output files
```
echo 'hello' > input.txt
./encoder.py < input.txt > encoded.txt
```

To decode any string, you just send it to decoder script
```
./decoder.py < encoded.txt
```


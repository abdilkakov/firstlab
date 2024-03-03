import os

with open('Example.txt', 'r') as r:
    with open('Examplefile_copy.txt', 'w') as w:
        for line in r:
            w.write(line)
import os

filename = '../README.md'
out = './README.md'
if not os.path.isfile(filename):
    exit(-1)
with open(filename, 'rw') as f:
    line = f.readline()
    idnum = 1
    with open(out, 'wa') as out:
        while(line):
            idnum = idnum + 1
            if idnum > 11:
                lineArr = line.split('|')
                lineArr[3] = ''
                lineArr[4] = ''
                out.write(" | ".join(lineArr))
                out.flush()
            line = f.readline()

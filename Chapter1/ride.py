"""
ID: lukassn1
LANG: PYTHON2
TASK: ride
PROG: ride
"""
with open('ride.in', 'r') as f:
    content = f.readlines()

lst = [content[i:i + 2] for i in xrange(0, len(content), 2)]

fout = open ('ride.out', 'w')

for item in lst:
    comet = item[0].strip()
    cmtNumbers = [ord(comet[i]) - 64 for i in xrange(0, len(comet))]
    cmtRes = reduce(lambda x, y: x*y, cmtNumbers, 1) % 47
    group = item[1].strip()
    grpNumbers = [ord(group[i]) - 64 for i in xrange(0, len(group))]
    grpRes = reduce(lambda x, y: x*y, grpNumbers, 1) % 47
    if (cmtRes == grpRes):
        fout.write ("GO" + '\n')
    else:
        fout.write ("STAY" + '\n')

fout.close()


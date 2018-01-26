
from sys import stdin

i = 0
for line in stdin:
    line_splitted = line.strip().split(' ')
    if i == 0:
        st = int(line_splitted[0])
    if i == 4:
        end = int(line_splitted[1])
        print('{0} {1} {2}'.format(st, end, line_splitted[2][:-3]))
    i = (i + 1) % 5
    

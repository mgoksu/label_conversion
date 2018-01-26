
from sys import stdin

window = 1e7
i = 0
print('#')
for line in stdin:
    line_splitted = line.strip().split(' ')
    if i == 4:
        end = int(line_splitted[1])
        info = line_splitted[2]
        mono = info[info.index('-') + 1: info.index('+')]
        print('{0:.2f} 125 {1}'.format(end / window, mono))
    i = (i + 1) % 5
    

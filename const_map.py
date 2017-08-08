# This is ugly but it's only a one time use script

from collections import defaultdict
import re

pat = re.compile('\s*(\S+)\s*=([-\d]+)\s+ # from enum (\S+)')


file = '/Users/dane/AppData/Local/Temp/gen_py/3.6/5AE2215C-270C-470B-A2B6-609A964E53A2x0x13x0.py'

d = defaultdict(dict)
lineno = 0
with open(file) as fp:
    l = fp.readline()
    lineno += 1
    while 'class constants' not in l:
        l = fp.readline()

    for l in fp.readlines():
        lineno += 1
        match = pat.search(l)
        if match:
            (value, ix, group) = match.groups()
            d[group][ix] = value
        else:
            print('Failed on line {}'.format(lineno))
            print(l)
            break

print('processed {} lines'.format(lineno))

with open('cmap.py', 'w') as fp:
    print("""
# This file defines functions which can reverse map AWRDE api enumerations to strings
#
# generated automatically by pyawr/const_map.py and should not be manually edited.
#
# This file will raise an exception if an illegal value is passed in.""", file=fp)
    for k in sorted(d.keys()):
        print('\n\ndef {}(value):'.format(k), file=fp)
        print('    items = {', file=fp)
        for k, v in d[k].items():
            print('             {}: "{}",'.format(k, v), file=fp)
        print('            }', file=fp)
        print('    return items[value]', file=fp)

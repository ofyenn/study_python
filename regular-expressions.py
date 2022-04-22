"""

Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

"""

import sys
import re

parrent = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    match_object = re.search(parrent, line)
    if match_object is not None:
        print(line)




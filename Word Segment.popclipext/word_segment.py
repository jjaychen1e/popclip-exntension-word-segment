from wordsegment import load, segment
import re
import sys

words = sys.argv[1]
load()
words = re.split('(\.|\!|\?|\,)', words)
res = []
for w in words:
    if '.' in w or '!' in w or '?' in w or ',' in w:
        res[-1] += w
    else:
        res.append(" ".join(segment(w)))
print(" ".join(res))
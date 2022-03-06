from wordsegment import load, segment
import re
import sys
from typing import *

def split_words(words: str):
    return re.split('(\.|\!|\?|\,|\:|\ |\(.*?\)|\[.*?\]|\{.*?\}|\'.*?\'|\".*?\"|`.*?`|\ \-\ |\/|\\\\)', words)

def join_words(words: List[str]) -> str:
    res: str = ""
    skip_space: bool = False
    for w in words:
        if  len(w) > 0 and \
            w[0] == '(' or \
            w[0] == '[' or \
            w[0] == '{':
            res += w
        elif w == '/' or w == '\\':
            res += w
            skip_space = True
        else:
            if skip_space:
                res += w
                skip_space = False
            else:
                res += " " + w
    return res.strip()

def process(words: List[str]) -> List[str]:
    func_result: List[str] = []
    for w in words:
        if '.' in w or '!' in w or '?' in w or ',' in w or ':' in w:
            func_result[-1] += w
        elif ' ' in w:
            continue
        elif w == '/' or w == '\\':
            func_result.append(w)
        elif w == '-':
            func_result.append('-')
        elif len(w) >= 2:
            if  w[0] == '(' and w[-1] == ')' or \
                w[0] == '[' and w[-1] == ']' or \
                w[0] == '{' and w[-1] == '}' or \
                w[0] == '"' and w[-1] == '"' or \
                w[0] == "'" and w[-1] == "'" or \
                w[0] == '`' and w[-1] == '`':
                local_result = process(split_words(w[1:-1]))
                local_result[0] = w[0] + local_result[0]
                local_result[-1] = local_result[-1] + w[-1]
                func_result.extend(local_result)
            else:
                func_result.append(join_words(segment(w)))
        elif w != '':
            func_result.append(join_words(segment(w)))
    return func_result

words = sys.argv[1]
load()
words = split_words(words)
# print(words)
res = process(words)

print(join_words(res), end="")

import sys
import re

rex = re.compile('((?:ARC\+CPSY\+DC|HPC|PRO|OS|MEPA)-\d+)')

data = {}
session_content = ""

with open("os.txt") as f:
    for line in f:
        mo = rex.match(line)
        if mo:
            session_name = mo.group(1)
            data[session_name] = line
        else:
            data[session_name] += line


for session_name in data:
    text = data[session_name]
    text = text.strip()
    text = text.replace('\n', '<br />')
    data[session_name] = text


with open("schedule-overview.md") as fin:
    text = fin.read()
    for session_name in data:
        text = text.replace(session_name, data[session_name])

    print text

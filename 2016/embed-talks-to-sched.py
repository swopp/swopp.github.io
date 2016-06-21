# vim:set expandtab ts=4 sw=4:
import sys
import re


rex = re.compile('((?:ARC\+CPSY\+DC|HPC|PRO|OS|MEPA)-\d+)')

data = {}
session_content = ""

sigs = [ "HPC", "OS" ]
for sig in sigs:
    path = "sigs/%s.txt" % sig
    with open(path) as f:
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
    # skip the header
    fin.readline()
    fin.readline()
    fin.readline()
    fin.readline()
    fin.readline()

    text = fin.read()
    for session_name in data:
        # add a space not to repalce HPC-11 with HPC-1
        text = text.replace(session_name + ' ', data[session_name])

    print text

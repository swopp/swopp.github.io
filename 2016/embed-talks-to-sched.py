# vim:set expandtab ts=4 sw=4:
import sys
import re


rex = re.compile('((?:ARC\+CPSY\+DC|HPC|PRO|OS|MEPA|BoF)-\d+)')

data = {}
session_content = ""

sigs = [ "HPC", "OS", "ARC+CPSY+DC", "PRO", "MEPA", "BoF" ]
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


output = ''
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

    output = text


# keep the header
header = ''
with open('schedule-details.md') as f:
    header += f.readline()
    header += f.readline()
    header += f.readline()
    header += f.readline()
    header += f.readline()

with open('schedule-details.md', 'r+') as f:
    f.write(header)
    f.write(output)

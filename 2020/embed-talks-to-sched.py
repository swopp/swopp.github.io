# vim:set expandtab ts=4 sw=4:
import sys
import re
import unicodedata


rex = re.compile('((?:ARC\+CPSY\+DC|HPC|PRO|OS|MEPA|BoF|xSIG)-\d+)')

data = {}

sigs = [ "HPC", "OS", "ARC+CPSY+DC", "PRO", "MEPA", "BoF", "xSIG" ]
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

    table_text = fin.read()
    for session_name in data:
        # add a space not to repalce HPC-11 with HPC-1
        table_text = table_text.replace(session_name + ' ', data[session_name])


# keep the header
header = ''
with open('schedule-details.md') as f:
    header += f.readline()
    header += f.readline()
    header += f.readline()
    header += f.readline()
    header += f.readline()

with open('schedule-details.md', 'w') as f:
    f.write(unicodedata.normalize('NFC', header))
    f.write(unicodedata.normalize('NFC', table_text))

from bs4 import BeautifulSoup
from string import printable
import requests

found = [{} for _ in range(100)]

for _ in range(5):
    res = requests.get('http://challs.bcactf.com:30831/flag?')
    soup = BeautifulSoup(res.text, features="html.parser")
    soup = BeautifulSoup(res.content, 'html.parser')
    text = soup.get_text()
    content = text.replace('\n', '')[42:]
    content = [content[i:i+12] for i in range(0, len(content), 12)]

    for i, c in enumerate(content):
        for l in printable:
            for j in range(12):
                b = ord(l)
                b = b << 4 ^ ((b << 4 & 0xff) >> 4)
                bm = 1 << j
                cb = b ^ bm
                out = bin(cb)[2:].zfill(12)
                if out == c:
                    if l not in found[i].keys():
                        found[i][l] = 1
                    else:
                        found[i][l] += 1

for f in found:
    if f:
        top_key = sorted(f, key=f.get, reverse=True)[0]
        print(top_key, end='')
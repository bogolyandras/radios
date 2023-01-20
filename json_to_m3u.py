import json
import os

with open('radios.json', 'r', encoding='utf-8') as f:
    radiosJson = json.load(f)

if radiosJson is None:
    raise Exception()

if not os.path.exists("generated"):
    os.mkdir("generated")

with open('generated/radios.m3u', 'w', encoding='utf-8') as f:
    f.write('#EXTM3U')
    f.write('\n')
    f.write('\n')
    for child in radiosJson['radios']:
        f.write('#EXTINF:,')
        f.write(child['title'])
        f.write('\n')
        f.write(child['url'])
        f.write('\n')
        f.write('\n')

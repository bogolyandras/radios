import os
import xml.etree.ElementTree as ET
import json
import xml.dom.minidom as md

with open('radios.json', 'r', encoding='utf-8') as f:
    radiosJson = json.load(f)

if radiosJson is None:
    raise Exception()

root = ET.Element('playlist')
root.set('version', '1')

title = ET.SubElement(root, 'title')
title.text = radiosJson['title']

trackList = ET.SubElement(root, 'trackList')

for child in radiosJson['radios']:
    track = ET.SubElement(trackList, 'track')
    title = ET.SubElement(track, 'title')
    title.text = child['title']
    location = ET.SubElement(track, 'location')
    location.text = child['url']

if not os.path.exists("generated"):
    os.mkdir("generated")

FILE_NAME = 'generated/radios.xspf'
tree = ET.ElementTree(root)
tree.write(FILE_NAME, encoding='utf-8')

pretty_xml = md.parse(FILE_NAME).toprettyxml(encoding='utf-8')
with open(FILE_NAME, 'bw') as f:
    f.write(pretty_xml)

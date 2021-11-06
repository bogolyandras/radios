import xml.etree.ElementTree as ET
import json

class Radio:
    title = ''
    url = ''

    def __str__(self):
        return 'title: ' + self.title + ', url: ' + self.url


class RadioEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Radio):
            return {'title': obj.title, 'url': obj.url}
        return json.JSONEncoder.default(self, obj)


tree = ET.parse('radios.xspf')
root = tree.getroot()
tree.getroot()

trackList = None
title = None

for elements in root:
    if 'trackList' in elements.tag:
        trackList = elements
    if 'title' in elements.tag:
        title = elements

if trackList is None:
    raise Exception()
if title is None:
    raise Exception()

radios = []
for track in trackList:
    radio = Radio()
    for trackElement in track:
        if 'title' in trackElement.tag:
            radio.title = trackElement.text
        if 'location' in trackElement.tag:
            radio.url = trackElement.text
    radios.append(radio)

with open('radios.json', 'w', encoding='utf-8') as f:
    json.dump({'title':title.text,'radios':radios},
              f, cls=RadioEncoder, ensure_ascii=False, indent=4)

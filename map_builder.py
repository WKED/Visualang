import glob
import os
import json

json_map = {}
for match in glob.glob('media/*.svg'):
    file_name = os.path.splitext(match)[0].split('\\')[1]
    json_map[file_name] = match

json_data = json.dumps(json_map, indent=4, sort_keys=True)
with open('map.json', 'a+') as file:
    file.write(json_data)

import json
import os
import re


target_file_names = os.listdir(path='./areas')
for target_file_name in target_file_names:
    result = []
    json_open = open(f"./areas/{target_file_name}", "r", encoding="utf-8")
    prefecture_dict = json.load(json_open)
    for url in prefecture_dict.values():
        for statuses in url.values():
            for status in statuses:
                if "POLYGON" in status["value"]:
                    polygon = status["value"]
                    coordinates = polygon.split(",") # ['POLYGON((139.81666667000002 35.74978875', '139.81667097 35.74978311'...]
                    for coordinate in coordinates: 
                        coordinate = re.findall("\d+\.\d+", coordinate)
                        latlng = {
                            "lat": float(coordinate[1]),
                            "lng": float(coordinate[0]),
                        }
                        result.append(latlng)

    with open(f"./extracted_polygons/{target_file_name}", "w") as file:
        json.dump(result, file, indent=4)

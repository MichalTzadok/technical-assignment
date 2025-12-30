import json


def dd_to_dms(value, is_latitude):
    """
    Convert decimal degrees to degrees, minutes, seconds.
    """
    direction = ""
    if is_latitude:
        direction = "N" if value >= 0 else "S"
    else:
        direction = "E" if value >= 0 else "W"

    value = abs(value)
    degrees = int(value)
    minutes_float = (value - degrees) * 60
    minutes = int(minutes_float)
    seconds = round((minutes_float - minutes) * 60, 2)

    return [degrees, minutes, seconds, direction]


def convert_coordinates(data):
    result = {}

    for location, values in data.items():
        lon, lat = values["dd"]

        dms_lon = dd_to_dms(lon, is_latitude=False)
        dms_lat = dd_to_dms(lat, is_latitude=True)

        result[location] = {
            "dd": values["dd"],
            "dms": [dms_lon, dms_lat]
        }

    return result


if __name__ == "__main__":
    with open("data.json", "r") as file:
        data = json.load(file)

    converted = convert_coordinates(data)

    print(json.dumps(converted, indent=2))

import json
import xml.etree.ElementTree as ET

def parse_element(element):
    data = {}
    if element.attrib:
        data["@attributes"] = element.attrib
    if element.text:
        data["text"] = element.text.strip()
    for child in element:
        child_data = parse_element(child)
        if child.tag in data:
            if not isinstance(data[child.tag], list):
                data[child.tag] = [data[child.tag]]
            data[child.tag].append(child_data)
        else:
            data[child.tag] = child_data
    return data

def convert_xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    json_data = json.dumps(parse_element(root), indent=4)
    return json_data



if __name__ == "__main__":
    with open("example.xml", 'r') as file:
        xml_string = file.read()

    json_data = convert_xml_to_json(xml_string)
    #print(json_data)

    # to validate https://jsonformatter.org/
    with open("example.json", 'w') as file:
        file.write(json_data)

    print("Saved in 'example.json'")

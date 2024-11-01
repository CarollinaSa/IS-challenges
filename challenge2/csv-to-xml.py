import csv
import xml.etree.ElementTree as ET

def csv_para_xml(csv_file, xml_file):
    root = ET.Element("WineData")

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            item = ET.SubElement(root, "Wine")
            for key, value in row.items():
                clean_key = key.strip().replace(" ", "_")
                child = ET.SubElement(item, clean_key)
                child.text = str(value).strip()
    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    indent(root)

    tree = ET.ElementTree(root)
    with open(xml_file, "wb") as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)

csv_file = "winequality-red.csv"
xml_file = "winequality-red.xml"
csv_para_xml(csv_file, xml_file)

print("Complete CSV to XML Conversion.")

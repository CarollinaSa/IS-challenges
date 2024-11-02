import xml.etree.ElementTree as ET


def create_xml_subset(input_xml, output_xml, quality_filter):
    # Load the original XML
    tree = ET.parse(input_xml)
    root = tree.getroot()

    # Create a new root for the subset XML
    new_root = ET.Element("WineData")

    # Filter elements based on quality
    for wine in root.findall("Wine"):
        quality = int(wine.find("quality").text)
        if quality == quality_filter:
            new_root.append(wine)

    # Save the subset as a new XML file
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_xml, encoding="utf-8", xml_declaration=True)
    print(f"Subset XML created at '{output_xml}' with quality {quality_filter}")


# Use the function with your XML file to create a subset with quality 5
input_xml = "winequality-red.xml"
output_xml = "filter_quality_5.xml"
create_xml_subset(input_xml, output_xml, quality_filter=5)


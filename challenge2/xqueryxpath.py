from lxml import etree

tree = etree.parse("winequality-red.xml")

quality_5_wines = tree.xpath("//Wine[quality='5']")

sub_xml_root = etree.Element('FilteredWines')

for wine in quality_5_wines:
    sub_xml_root.append(wine)

sub_xml_str = etree.tostring(sub_xml_root, pretty_print=True, xml_declaration=True, encoding='UTF-8')

with open("filtered_winequality.xml", 'wb') as f:
    f.write(sub_xml_str)

print("New XML file 'filtered_winequality.xml' created successfully.")

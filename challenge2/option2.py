from lxml import etree

def apply_xslt(input_xml, xslt_file, output_xml):
    # Load the XML and XSLT files
    xml_tree = etree.parse(input_xml)
    xslt_tree = etree.parse(xslt_file)
    transform = etree.XSLT(xslt_tree)

    # Apply the transformation
    new_tree = transform(xml_tree)

    # Save the result
    new_tree.write(output_xml, pretty_print=True, encoding="utf-8", xml_declaration=True)
    print(f"Transformed XML saved at '{output_xml}'")

# Use the function with your XML and XSLT files
input_xml = "winequality-red.xml"
xslt_file = "filter_quality_5.xslt"
output_xml = "subset_quality_5_xslt.xml"
apply_xslt(input_xml, xslt_file, output_xml)

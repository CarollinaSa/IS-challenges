from lxml import etree


def apply_xslt(xml_file, xslt_file, output_file):
    xml_tree = etree.parse(xml_file)
    xslt_tree = etree.parse(xslt_file)

    transform = etree.XSLT(xslt_tree)

    result_tree = transform(xml_tree)

    with open(output_file, "wb") as f:
        f.write(etree.tostring(result_tree, pretty_print=True, encoding="UTF-8", xml_declaration=True))

    print(f"Output saved to {output_file}.")


xml_file = "winequality-red.xml"
xslt_file = "xquery.xslt"
output_file = "output.xml"
apply_xslt(xml_file, xslt_file, output_file)

from lxml import etree


def xpath(sub_xml_1):
    tree = etree.parse("winequality-red.xml")

    good_quality = tree.xpath("Wine[quality='5']")
    print("Quality is greater than 5:")

    good_quality_root = etree.Element("GoodQuality")

    for quality in good_quality:
        good_quality_root.append(quality)
        print(etree.tostring(quality, pretty_print=True).decode("utf-8"))

    good_quality_tree = etree.ElementTree(good_quality_root)
    with open(sub_xml_1, "wb") as f:
        good_quality_tree.write(f, encoding="utf-8", xml_declaration=True)

from lxml import etree

tree = etree.parse("winequality-red.xml")

quality_5_wines = tree.xpath("//Wine[quality='5']")
print("Wines with quality 5:")
for wine in quality_5_wines:
    print(etree.tostring(wine, pretty_print=True).decode("utf-8"))

high_alcohol_wines = tree.xpath("//Wine[alcohol > 10]")
print("\nWines with alcohol content > 10:")
for wine in high_alcohol_wines:
    print(etree.tostring(wine, pretty_print=True).decode("utf-8"))

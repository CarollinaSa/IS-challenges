from lxml import etree

# Load the XML file
tree = etree.parse("winequality-red.xml")

# Example 1: Select wines with quality score of 5
quality_5_wines = tree.xpath("//Wine[quality='5']")
print("Wines with quality 5:")
for wine in quality_5_wines:
    print(etree.tostring(wine, pretty_print=True).decode("utf-8"))

# Example 2: Select wines with alcohol content > 10
high_alcohol_wines = tree.xpath("//Wine[alcohol > 10]")
print("\nWines with alcohol content > 10:")
for wine in high_alcohol_wines:
    print(etree.tostring(wine, pretty_print=True).decode("utf-8"))

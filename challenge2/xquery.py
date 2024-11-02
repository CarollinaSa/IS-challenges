from lxml import etree

# Load the XML file
tree = etree.parse("winequality-red.xml")

# Use XPath to select all wines with quality = 5
quality_5_wines = tree.xpath("//Wine[quality='5']")

print("Wines with quality = 5:")
for wine in quality_5_wines:
    # Extract specific fields
    fixed_acidity = wine.find("fixed_acidity").text
    alcohol = wine.find("alcohol").text
    quality = wine.find("quality").text

    print(f"<Wine>\n  <fixed_acidity>{fixed_acidity}</fixed_acidity>\n  <alcohol>{alcohol}</alcohol>\n  <quality>{quality}</quality>\n</Wine>")

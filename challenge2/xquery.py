from lxml import etree

tree = etree.parse("winequality-red.xml")

quality_5_wines = tree.xpath("//Wine[quality='5']")

print("Wines with quality = 5:")
for wine in quality_5_wines:
    fixed_acidity = wine.find("fixed_acidity").text
    alcohol = wine.find("alcohol").text
    quality = wine.find("quality").text

    print(f"<Wine>\n  <fixed_acidity>{fixed_acidity}</fixed_acidity>\n  <alcohol>{alcohol}</alcohol>\n  <quality>{quality}</quality>\n</Wine>")

import xml.dom.minidom as minidom

def xml_to_text(file_path):
    try:
        dom_tree = minidom.parse(file_path)
        root = dom_tree.documentElement

        def extract_text(node):
            text = ""
            if node.nodeType == node.ELEMENT_NODE:
                for child in node.childNodes:
                    if child.nodeType == child.TEXT_NODE:
                        text += child.nodeValue.strip() + " "
                    else:
                        text += extract_text(child)
            return text

        return extract_text(root).strip()

    except Exception as e:
        return f"Error processing XML file: {e}"

file_path = "321gone.xml"
result = xml_to_text(file_path)
print(result)

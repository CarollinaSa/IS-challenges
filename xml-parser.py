import xml.dom.minidom as minidom

# Função para converter XML para texto sem tags
def xml_para_texto_simples(file_path):
    try:
        dom_tree = minidom.parse(file_path)
        root = dom_tree.documentElement

        def extrair_texto(node):
            texto = ""
            if node.nodeType == node.ELEMENT_NODE:
                for child in node.childNodes:
                    if child.nodeType == child.TEXT_NODE:
                        texto += child.nodeValue.strip() + " "
                    else:
                        texto += extrair_texto(child)
            return texto

        return extrair_texto(root).strip()

    except Exception as e:
        return f"Erro ao processar o ficheiro XML: {e}"

file_path = "321gone.xml"
resultado = xml_para_texto_simples(file_path)
print(resultado)

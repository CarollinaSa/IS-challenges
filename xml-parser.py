import xml.dom.minidom as minidom


# Função para converter XML para texto usando DOM
def xml_para_texto(file_path):
    try:
        dom_tree = minidom.parse(file_path)

        root = dom_tree.documentElement

        def extrair_texto(node, indent=0):
            texto = ""
            if node.nodeType == node.ELEMENT_NODE:
                texto += "  " * indent + f"<{node.tagName}>"

                if node.hasChildNodes():
                    for child in node.childNodes:
                        if child.nodeType == child.TEXT_NODE:
                            texto += child.nodeValue.strip()
                        else:
                            texto += "\n" + extrair_texto(child, indent + 1)
                    texto += "\n" + "  " * indent + f"</{node.tagName}>"
                else:
                    texto += f"</{node.tagName}>"
            return texto

        return extrair_texto(root)

    except Exception as e:
        return f"Erro ao processar o ficheiro XML: {e}"


file_path = "caminho_para_o_teu_ficheiro.xml"
resultado = xml_para_texto(file_path)
print(resultado)

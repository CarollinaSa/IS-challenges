import xmlschema


def validar_xml(xml_file, xsd_file):
    try:
        schema = xmlschema.XMLSchema(xsd_file)
        is_valid = schema.is_valid(xml_file)

        if is_valid:
            print("O XML é válido de acordo com o Schema!")
        else:
            print("O XML NÃO é válido de acordo com o Schema.")
            print(schema.validate(xml_file))

    except Exception as e:
        print(f"Erro ao validar XML: {e}")


xml_file = "winequality-red.xml"
xsd_file = "winequality-schema.xsd"
validar_xml(xml_file, xsd_file)

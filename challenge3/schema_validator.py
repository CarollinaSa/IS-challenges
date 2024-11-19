import xmlschema
def validar_xml(xml_file, xsd_file):
    try:
        schema = xmlschema.XMLSchema(xsd_file)
        is_valid = schema.is_valid(xml_file)

        if is_valid:
            print("XML is valid according to Schema!")
        else:
            print("XML is NOT valid according to Schema.")
            print(schema.validate(xml_file))

    except Exception as e:
        print(f"Error validating XML: {e}")


xml_file = "winequality-red.xml"
xsd_file = "winequality-schema.xsd"
validar_xml(xml_file, xsd_file)

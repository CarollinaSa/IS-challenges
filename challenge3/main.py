import os

from challenge2.csv_to_xml import csv_para_xml
from challenge2.schema_validator import validar_xml
from challenge2.xquery import apply_xslt
from challenge2.xpath import xpath


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        print('Choose an option:')
        print('1. Turn CSV to XML')
        print('2. Use schema to validate XML')
        print('3. Use xpath to get xml')
        print('4. Use xquery to get xml')
        print('5. Exit')
        match int(input('Enter: ')):
            case 1:
                csv_para_xml("winequality-red.csv", "winequality-red.xml")
            case 2:
                validar_xml("winequality-red.xml", "winequality-schema.xsd")
            case 3:
                xpath("winequality-red.xml")
            case 4:
                apply_xslt("winequality-red.xml", "filtered_quality.xslt", "Filtered_Wine.xml")
            case 5:
                print('Goodbye!')
                break


if __name__ == '__main__':
    main()

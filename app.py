import xml.etree.ElementTree as ET
import sys

def xml_to_custom_language(xml_string):
    try:
        root = ET.fromstring(xml_string)
        # return process_element(root)
        return "\n".join(process_element(child) for child in root)
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {e}")

def process_element(elem):
    print(elem.tag)
    if elem.tag == "array":
        return process_array(elem)
    elif elem.tag == "dictionary":
        return process_dictionary(elem)
    elif elem.tag == "string":
        return process_string(elem)
    elif elem.tag == "constant":
        return process_constant(elem)
    elif elem.tag == "comment":
        return process_comment(elem)
    else:
        raise ValueError(f"Unknown XML element: {elem.tag}")

def process_array(elem):
    values = ", ".join(child.text for child in elem)
    return f"<< {values} >>"

def process_dictionary(elem):
    entries = [
        f"{entry.attrib['name']} => {entry.text}"
        for entry in elem
    ]
    return "table(\n  " + ",\n  ".join(entries) + "\n)"

def process_string(elem):
    return f"@\"{elem.text}\""

def process_constant(elem):
    return f"const {elem.attrib['name']} = {elem.text};"

def process_comment(elem):
    return f"{{#\n {elem.text}\n#}}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]

    # Чтение XML из стандартного ввода
    print("Введите XML (Ctrl+D для завершения ввода):")
    xml_input = sys.stdin.read()
    # with open("./input_file.xml", "r") as file:
    #     xml_input = file.read()
    # print(xml_input)

    # Преобразование XML
    try:
        custom_language = xml_to_custom_language(xml_input)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Запись результата в файл
    with open(output_file, "w") as f:
        f.write(custom_language)

    print(f"Преобразование завершено. Результат сохранен в {output_file}.")

if __name__ == "__main__":
    main()

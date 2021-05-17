documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "2200 076234", "name": "Иван Давнов"},
    {"type": "invoice", "number": "12-3", "name": "Пи Качу"},
    {"type": "insurance", "number": "10000", "name": "Павел Аристархов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': [],
    '4': ["2200 076234", "12-3", "10000"],
}


def print_menu():
    message = "p – people – ввести номер документа и получить имя человека, которому он принадлежит\n" \
              "s – shelf – ввести номер документа и получить номер полки, на которой он находится\n" \
              "l – list – вывести список всех документов в формате passport \"2207 876234\" \"Имя\"\n" \
              "a – add – добавить новый документ в каталог и в перечень полок\n" \
              "d – delete – ввести номер документа и удалить его из каталога и из перечня полок\n" \
              "m – move – ввести номер документа и целевую полку и переместить его с текущей полки на целевую.\n" \
              "as – add shelf – ввести номер новой полки и добавить ее в перечень.\n" \
              "exit - закрыть программу"
    print(message)


def get_people(number, documents):
    people = f"документ №{number} не найден"
    for doc in documents:
        if number == doc["number"]:
            people = doc["name"]
            break
    return people


def search_document(number, directories):
    document = f"документ №{number} не найден"
    number_ = str(number)
    for i, doc in directories.items():
        if number_ in doc:
            document = f"документ №{number} на полке №{i}"
            break
    return document


def get_list_documents(input_documents):
    out_line = "Тип документа \t\t № документа \t\t ФИО\n"
    out_line += "\n".join(
        [f"\"{doc['type']}\"\t\t\"{doc['number']}\"\t\t\"{doc['name']}\"" for doc in input_documents]) + "\n"
    return out_line


def add_document(type_doc="", name_person="", number="", direct="", documents="", directories=""):
    if "" in locals().values():
        return "Введен не полный набор данных"
    if not type_doc in ("passport", "insurance", "invoice"):
        return "некорректный тип документа"
    if not direct in directories:
        yes_or_no = input("Нет такой полки. Ходите добавить новую полку с таким идентификатором? (y/n): ").lower()
        if yes_or_no in ("y", "yes", "да", "д"):
            print(add_shelf(direct, directories))
        else:
            return "Данные не добавлены"
    documents.append({"type": type_doc, "number": number, "name": name_person})
    directories[direct].append(number)
    return "Данные добавлены"


def move_document(number, direct, directories):
    out_line = f"документ №{number} не найден"
    if not direct in directories:
        yes_or_no = input("Нет такой полки. Ходите добавить новую полку с таким идентификатором? (y/n): ").lower()
        if yes_or_no in ("y", "yes", "да", "д"):
            print(add_shelf(direct, directories))
        else:
            return "Документы не добавлены"
    for id, line in directories.items():
        if number in line:
            directories[id].remove(number)
            directories[direct].append(number)
            out_line = f"документ №{number} перемещён на полдку №{direct}"
            break
    return out_line


def delete_line(number, documents, directories):
    out_line = f"документ №{number} не найден"
    for id_doc, doc in enumerate(documents):
        if doc["number"] == number:
            del (documents[id_doc])
            out_line = f"документ №{number} удалён "
            break
    for id_line, line in directories.items():
        if number in line:
            directories[id_line].remove(number)
            out_line += f"с полки №{id_line}"
            break
    return out_line


def add_shelf(number, directories):
    if number in directories:
        return "Уже есть такая полка"
    else:
        directories[number] = []
        return "Добавлено"


def main(documents, directories):
    print_menu()
    while True:
        input_str = input("Ваша команда: ").lower()
        if input_str == "exit":
            break
        elif input_str in ("p", "people"):
            print(get_people(input("Укажите номер документа: "), documents))
        elif input_str in ("s", "self"):
            print(search_document(input("Укажите номер документа: "), directories))
        elif input_str in ("l", "list"):
            print(get_list_documents(documents))
        elif input_str in ("a", "add"):
            temp_data = [str(x).strip() for x in
                         input("Введите Тип, номер, ФИО и полку нового документа через запятую:\n").split(",")]
            if len(temp_data) >= 4:
                t, n, f, d, *_ = temp_data
                print(add_document(t, n, f, d, documents, directories))
            else:
                print("Введен не полный набор данных!\n")
        elif input_str in ("d", "delete"):
            print(delete_line(input("Введите номер документа к удалению: "), documents, directories))
        elif input_str in ("m", "move"):
            temp_data = [str(x).strip() for x in
                         input("Введите номер документа и новую полку через запятую:\n").split(",")]
            if len(temp_data) >= 2:
                n, d, *_ = temp_data
                print(move_document(n, d, directories))
            else:
                print("Введен не полный набор данных!\n")
        elif input_str in ("as", "add shelf"):
            add_shelf(input("Введите номер новой полки"), directories)


if __name__ == "__main__":
    main(documents, directories)

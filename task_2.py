# TODO импортировать необходимые молули
import os.path
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data_json = list()

    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as file:
        dictionaries = csv.DictReader(file)
        for dictionary in dictionaries:
            current_dictionary = dict()
            for key in dictionary:
                current_dictionary[key] = dictionary[key]
            data_json.append(current_dictionary)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as file:
          json.dump(data_json, file, indent=4, ensure_ascii=True)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

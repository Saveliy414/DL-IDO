# TODO решите задачу
import os.path
import json
def task() -> float:
    result = 0.0
    with open('input.json', 'r') as fail:
        json_dictionaries = json.load(fail)
        for dictionary in json_dictionaries:
            result += dictionary['score'] * dictionary['weight']

    return result


print(f'{task():.3f}')

# TODO Напишите функцию find_common_participants

def find_common_participants(participant_1, participant_2, separator=','):
    result = []
    splited_participant_1 = participant_1.split(separator)
    splited_participant_2 = participant_2.split(separator)
    for name in splited_participant_1:
        if splited_participant_2.__contains__(name):
            result.append(name)
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group)
common_participants.sort()
print(common_participants)
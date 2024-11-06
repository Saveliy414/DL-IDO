# TODO Напишите функцию find_common_participants

def find_common_participants(participant_1, participant_2, separator=','):
    result = list()
    splited_participant_1 = participant_1.split(separator)
    splited_participant_2 = participant_2.split(separator)
    for name in splited_participant_1:
        if name in splited_participant_2:
            result.append(name)
    result.sort()
    return result


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group_1 = "Иванов|Петров|Сидоров"
participants_second_group_2 = "Петров|Сидоров|Смирнов"
common_participants_1 = find_common_participants(participants_first_group_1, participants_second_group_2, '|')
print(common_participants_1)


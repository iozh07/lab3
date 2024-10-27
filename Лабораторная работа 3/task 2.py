# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, splitter=","):
    participants_first_group = set(participants_first_group.split(splitter))
    participants_second_group = set(participants_second_group.split(splitter))
    common = participants_first_group & participants_second_group
    common = sorted(list(common))
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group, participants_second_group, splitter="|")
print(common)
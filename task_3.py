# TODO  Напишите функцию count_letters
def count_letters(text):
    result = dict()
    for symbol in text:
      if symbol.isalpha():
          symbol = symbol.lower()
          if result.get(symbol) == None:
              result[symbol] = 1
          else:
              result[symbol] += 1
    return result

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dict):
    result = dict()
    total_letters = 0
    for value in letters_dict.values():
        total_letters += value

    for key in letters_dict.keys():
        result[key] = letters_dict[key] / total_letters

    return result

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

for key, value in calculate_frequency(count_letters((main_str))).items():
    print(f'{key}: {value:.2f}')




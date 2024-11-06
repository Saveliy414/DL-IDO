# TODO Напишите функцию для поиска индекса товара



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def find_product(items_list, item):
    index = 0
    for product in items_list:
        if product == item:
            return index
        index += 1
    return None

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_product(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

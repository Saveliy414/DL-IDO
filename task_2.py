# TODO Найдите количество книг, которое можно разместить на дискете
symbols = 100 * 50 * 25 * 4
capacity = 1.44 * 1024 * 1024
result = capacity / symbols
print("Количество книг, помещающихся на дискету:", (capacity // symbols).__int__())

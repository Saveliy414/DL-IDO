numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = 0
count = 0
sum = 0
for number in numbers:
    if (number == None):
        index = count
    else:
        sum += number
        count += 1

numbers[index] = sum / numbers.__len__()
print("Измененный список:",numbers)
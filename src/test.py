my_list = [10, 20, 30, 40, 50]

try:
    user_index = int(input("Введите индекс числа: "))
except ValueError:
    print("Ошибка: введен некорректный индекс!")
except IndexError:
    print("Ошибка: введен некорректный индекс!")
else:
    print(f"Элемент с индексом {user_index}: {my_list[user_index]}")
finally:
    print("Конец программы.")

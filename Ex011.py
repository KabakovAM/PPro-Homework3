dic_list = {'Фонарик': 1, 'Вода': 5, 'Еда': 1, 'Компас': 1, 'Одежда': 3}
data = int(input('Введите маскимальную грузоподъёмность рюкзока: '))
while data > 0:
    for key, value in dic_list.items():
        if value <= data:
            print(key)
            data -= value
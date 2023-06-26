dic_list = {'Федя': ('фонарик', 'еда', 'сендвич'), 'Вася': ('еда', 'компас'), 'Егор': ('компас', 'еда')}
a_set = set(dic_list['Федя'])
b_set = set(dic_list['Вася'])
c_set = set(dic_list['Егор'])
check = 0
print('Какие вещи взяли все три друга?')
print(*a_set.union(b_set, c_set))
print('Какие вещи уникальны, есть только у одного друга?')
print(*a_set.difference(b_set, c_set))
print('Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?')
for i in a_set.union(b_set, c_set):
    if i in a_set:
        check += 1
    if i in b_set:
        check += 1
    if i in c_set:
        check += 1
    if check == 2:
        for key, value in dic_list.items():
            if i not in value:
                print(f'{key} {i}')
    else:
        check = 0
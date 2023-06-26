def count_str(_str : str, i : str):
    count = -1
    for k in _str:
        if k == i:
            count += 1
    return count


_str = input('Введите текст: ')
dic_str = {}
for i in _str:
    if i in dic_str:
        continue
    else:
        dic_str[i] = 1
        dic_str[i] += count_str(_str, i)
print(dic_str)
for i in _str:
    if i in dic_str:
        continue
    else:
        dic_str[i] = 1
        dic_str[i] += _str.count(i) - 1 
print(dic_str)
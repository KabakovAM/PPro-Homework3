_str = input('Введите текст: ')
data = sorted(_str.split())
longest = len(max(data, key=len))
for i in range(len(data)):
    print(f'{i+1}) {data[i]:>{longest}}')

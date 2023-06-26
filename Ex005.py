data = [1, 2, 3, 2, 1, 5, 3, 6, 4]
data_1 = []
for i in range(len(data)):
    if data[i] % 2 == 0:
        data_1.append(i+1)
print(*data_1)
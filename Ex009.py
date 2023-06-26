num_list = [5, 2, 3, 1, 1, 3, 4, 5]
result_list = []
num_list.sort()
temp = None
for i in range(len(num_list)):
    if num_list[i] == temp:
        result_list.append(temp)
        temp = None
    else:    
        temp = num_list[i]
print(result_list)

from sys import argv

script, filename = argv

with open(filename, 'r') as temp:
    file_string = temp.read().replace('\n', ' ')

file_list = file_string.split()

data_list = [(file_list[0], 1)]
file_list.pop(0)

for i in file_list:
    found_it = False
    while found_it == False:
        for j in data_list:
            if i == j[0]:
                data_list[data_list.index(j)] = (i, j[1] + 1)
                found_it = True
                break
        if found_it == False:
            data_list.append((i, 1))
            break

print data_list
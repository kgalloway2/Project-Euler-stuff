list_to_sort = [20, 19, 18, 'd', 'g', 17, 'a', 16, 15, 14, 13, 'c', 12, 11, 'f', 'b', 10, 9, 8, 7, 6, 'e', 5, 4, 3, 2, 1]
# list_to_sort = ['b', 'a', 'd', 'f', 'g', 'e', 'c']

def which_key(list_to_sort):
    is_letter = False
    is_number = False
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in list_to_sort:
        if type(i) == int:
            is_number = True
        elif type(i) == str:
            is_letter = True
    if is_number and is_letter:
        return alpha, True
    elif is_number:
        return None, False
    elif is_letter:
        return alpha, False

def sorter(list_to_sort):
    unsorted = True
    key, split = which_key(list_to_sort)  

    if split:
        int_list = []
        count = 0
        length = len(list_to_sort) - 1
        while count <= length:
            if type(list_to_sort[count]) == int:
                int_list.append(list_to_sort.pop(list_to_sort.index(list_to_sort[count])))
                length = len(list_to_sort) - 1
            else:
                count += 1
        int_list = sorter(int_list)

    while unsorted:
        for i in list_to_sort:
            for j in list_to_sort[list_to_sort.index(i) + 1:]:
                if key == None:
                    a, b = i, j
                elif key != None:
                    a, b = key.index(i), key.index(j)
                if a > b:
                    list_to_sort[list_to_sort.index(j)] = i
                    list_to_sort[list_to_sort.index(i)] = j
                    break
        unsorted = False
        for i in list_to_sort:
            for j in list_to_sort[list_to_sort.index(i) + 1:]:
                if key == None:
                    a, b = i, j
                else:
                    a, b = key.index(i), key.index(j)
                if a > b:
                    unsorted = True
                    break
            if unsorted == True:
                break
    
    if split:
        list_to_sort = int_list + list_to_sort
    
    return list_to_sort

print sorter(list_to_sort)
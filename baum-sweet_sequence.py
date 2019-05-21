n = int(raw_input("Generate the Baum-Sweet sequence up to what number?"))

baumsweet_list = []

for i in range(0, n + 1):
    bin_i = bin(i)[2:]
    list_bin_i = bin_i.split("1")
    odd = 0
    for j in list_bin_i:
        if (len(j) % 2) == 0:
            pass
        elif (len(j) % 2) == 1:
            odd += 1
    if odd >= 1:
        baumsweet_list.append(0)
    else: 
        baumsweet_list.append(1)

print baumsweet_list
from sys import argv

script, file_1, file_2, similarity_threshold = argv

with open(file_1, 'r') as file_1_temp:
    file_1_string = file_1_temp.read().replace('\n', ' ')

with open(file_2, 'r') as file_2_temp:
    file_2_string = file_2_temp.read().replace('\n', ' ')

file_1_list = file_1_string.split(' ')
file_2_list = file_2_string.split(' ')

similarity_list =[]
n = 1

while n <= (len(file_1_list) - (int(similarity_threshold)-1)):
    m = 1
    while m <= (len(file_2_list) - (int(similarity_threshold)-1)):
        file_1_check = file_1_list[(n - 1):(n - 1 + int(similarity_threshold))]
        file_2_check = file_2_list[(m - 1):(m - 1 + int(similarity_threshold))]
        if file_1_check == file_2_check:
            similarity_list.append((file_1_check, n - 1, file_2_check, m - 1))
        m+= 1
    n += 1

for i in similarity_list:
    print "Here is a similarity: ", i 

if not similarity_list:
    print "There were no similarities of %s words in a row." % similarity_threshold
elif similarity_list:
    print "There were %d total similarities between %s and %s." % (len(similarity_list), file_1, file_2)
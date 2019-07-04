from sys import argv
from random import randint
import time

start = time.time()
script, filename = argv

with open(filename, 'r') as temp:
    file_string = temp.read().replace('\n', ' ')

file_list = file_string.split()

shuffled_list = []

count = 0
length = len(file_list)

while count < length:
    item = file_list.pop(randint(0, len(file_list) - 1))
    shuffled_list.append(item)
    count +=1

print shuffled_list
end = time.time()
print (end - start)
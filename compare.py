import re
on_youtube = open('onyoutube', 'r').read()
on_drive = open('comparetoyoutube.txt', 'r').read()


def convert_to_numbers(read_file):
    list = re.findall(r'\d+', read_file)
    numbers = []
    for i in list:
        num = int(i)
        if num > 999:
            numbers.append(num)
    return numbers

on_both = []

list_on_youtube = convert_to_numbers(on_youtube)
list_on_drive = convert_to_numbers(on_drive)
for i in list_on_youtube:
    if i in list_on_drive:
        on_both.append(i)

print sorted(on_both)
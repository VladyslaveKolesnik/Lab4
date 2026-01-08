text = input()
max_count = 0
result_char = ''
checked = []
for char in text:
    if char not in checked:
        count = text.count(char)
        if count > max_count:
            max_count = count
            result_char = char
        checked.append(char)
if result_char == ' ':
    print('пропуск', max_count)
else:
    print(result_char, max_count)
    
text = input()
text = text + " "
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
current_word = ""
min_word = ""
min_len = 10000

for char in text:
    if char in letters:
        current_word = current_word + char
    else:
        if len(current_word) > 0:
            if len(current_word) < min_len:
                min_word = current_word
                min_len = len(current_word)
            current_word = ""
print(min_word, min_len)

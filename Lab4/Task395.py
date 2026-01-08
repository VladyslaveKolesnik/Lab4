text = input()
count = 0
n = len(text)

for i in range(n):
    if text[i].isalpha():
        if i == 0 or not text[i-1].isalpha():
            count += 1
print(count)

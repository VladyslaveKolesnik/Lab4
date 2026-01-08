text = input("enter the string: ")
char = input()

answer = 0

for i in range(len(text)):
    if text[i] == char:
        answer = i + 1
        break
print(answer)

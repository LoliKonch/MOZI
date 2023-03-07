import itertools

input_message1 = "ооеов нбнзс дтжьи томде меов"
output_message1 = "возможно семь бед один ответ"
input_message2 = "дасрк мтане мрмшо птеуи удише оаа"
output_message2 = "да один пашет семеро руками машут"

input_message1 = input_message2.replace(" ", "")
print(len(input_message1))
letter_list1 = []
for letter in input_message1:
    letter_list1.append(letter)

table1 = [[], [], [], []]
for i in range(4):
    for j in range(7):
        table1[i].append(letter_list1[(i*7)+j])
for i in range(7):
    for j in range(4):
        print(table1[j][i], end='')
    print('')

perm_set = itertools.permutations(table1)
for one in perm_set:
    for i in range(7):
        for j in range(4):
            print(one[j][i], end='')
    print("END")



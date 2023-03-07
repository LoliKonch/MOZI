input_message = "ЖВАКИН И ЯРОВОЙ УЧИЛИСЬ ШИФРОВАТЬ"
input_message = input_message.replace(" ", "")

letter_list = []
for letter in input_message:
    letter_list.append(letter)
letter_list.append("Х")

table = [[], [], [], [], []]

for i in range(5):
    for j in range(6):
        table[i].append(letter_list[(i*6)+j])

for i in range(6):
    for j in range(5):
        print(table[j][i], end='')
    print(" ", end='')
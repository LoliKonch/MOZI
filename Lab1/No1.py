input_message = "ЖВАКИН И ЯРОВОЙ УЧИЛИСЬ ШИФРОВАТЬ"
input_message = input_message.replace(" ", "")

letter_list = list(input_message)
letter_list.append("Х")

table = [[], [], [], [], []]

for i in range(5):
    for j in range(6):
        table[i].append(letter_list[(i*6)+j])

for i in table:
    print(i)

for i in range(6):
    for j in range(5):
        print(table[j][i], end='')
    print(" ", end='')
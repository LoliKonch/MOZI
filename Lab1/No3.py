input_message = "ЖВАКИН И ЯРОВОЙ УЧИЛИСЬ"
input_message = input_message.replace(" ", "")

letter_list = list(input_message)

table = [["0", "3", "2", "4", "1", "5"], ["2"], ["4"], ["1"], ["3"]]
for i in range(1, 5):
    for j in range(1, 6):
        table[i].append(letter_list[((i - 1) * 5) + j - 1])

for i in range(5):
    for j in range(6):
        print(table[i][j], end='')
    print("")
print("\n")

table = sorted(table)

for i in range(5):
    for j in range(6):
        print(table[i][j], end='')
    print("")
print("\n")

new_table = [[], [], [], [], [], []]
for i in range(5):
    for j in range(6):
        new_table[j].append(table[i][j])

new_table = sorted(new_table)

for i in range(5):
    for j in range(6):
        print(new_table[j][i], end='')
    print("")
print("\n")

output_message = ""
for i in range(1, 6):
    for j in range(1, 5):
        output_message += new_table[i][j]

for slice in [5, 11, 17]:
    new = output_message[:slice] + " " + output_message[slice:]
    output_message = str(new)
print(output_message)
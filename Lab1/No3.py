input_message = "ЖВАКИН И ЯРОВОЙ УЧИЛИСЬ"
input_message = input_message.replace(" ", "")

letter_list = []
for letter in input_message:
    letter_list.append(letter)

table = [["0", "3", "2", "4", "1", "5"], ["2"], ["4"], ["1"], ["3"]]
for i in range(1, 5):
    for j in range(1, 6):
        table[i].append(letter_list[((i - 1) * 5) + j - 1])

print(table)
table = sorted(table)
print(table)

new_table = [[], [], [], [], [], []]
for i in range(5):
    for j in range(6):
        new_table[j].append(table[i][j])

print(new_table)
new_table = sorted(new_table)
print(new_table)

output_message = ""
for i in range(1, 6):
    for j in range(1, 5):
        output_message += new_table[i][j]

for slice in [5, 11, 17]:
    new = output_message[:slice] + " " + output_message[slice:]
    output_message = str(new)
print(output_message)
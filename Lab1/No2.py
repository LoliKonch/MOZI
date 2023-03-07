input_message = "ЖВАКИН И ЯРОВОЙ УЧИЛИСЬ"
input_message = input_message.replace(" ", "")

letter_list = []
for letter in input_message:
    letter_list.append(letter)

table = [["П"], ["И"], ["Т"], ["О"], ["Н"]]

for i in range(1, 5):
    for j in range(5):
        table[j].append(letter_list[((i-1)*5)+j])

table = sorted(table)
output_message = ""
for i in range(5):
    for j in range(1, 5):
        output_message += table[i][j]

for slice in [5, 11, 17]:
    new = output_message[:slice] + " " + output_message[slice:]
    output_message = str(new)
print(output_message)

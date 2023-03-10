input_message = "ЖВАКИН И ЯРОВОЙ УЧИЛИСЬ"
input_message = input_message.replace(" ", "")

letter_list = list(input_message)

table = [["П"], ["И"], ["Т"], ["О"], ["Н"]]

for i in range(1, 5):
    for j in range(5):
        table[j].append(letter_list[((i-1)*5)+j])

for i in range(5):
    for j in range(5):
        print(table[j][i], end='')
    print("")
print("\n")

table = sorted(table)


for i in range(5):
    for j in range(5):
        print(table[j][i], end='')
    print("")

output_message = ""
for i in range(5):
    for j in range(1, 5):
        output_message += table[i][j]
print("\n\n")

for slice in [5, 11, 17]:
    new = output_message[:slice] + " " + output_message[slice:]
    output_message = str(new)
print(output_message)

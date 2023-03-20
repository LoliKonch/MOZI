input_message = "жвакин и яровой учатся в университете"
input_message = input_message.replace(" ", "")
input_message = list(input_message)

m = [
    ["а", "р", "б", "у", "з", "в", "г", "д"],
    ["е", "ж", "и", "й", "к", "л", "м", "н"],
    ["о", "п", "с", "т", "ф", "х", "ц", "ч"],
    ["ш", "щ", "ь", "ы", "ъ", "э", "ю", "я"]]

for k in range(0, len(input_message), 2):
    x1 = -1
    x2 = -1
    y1 = -1
    y2 = -1
    for i in range(4):
        for j in range(8):
            if x1 == -1:
                if input_message[k] == m[i][j]:
                    x1 = i
                    y1 = j
            if x2 == -1:
                if input_message[k + 1] == m[i][j]:
                    x2 = i
                    y2 = j

    if x1 == x2:

        if y1 == 7:
            y1 = 0
            y2 += 1
        elif y2 == 7:
            y1 += 1
            y2 = 0
        else:
            y1 += 1
            y2 += 1

    elif y1 == y2:

        if x1 == 3:
            x1 = 0
            x2 += 1
        elif x2 == 3:
            x2 = 0
            x1 += 1
        else:
            x2 += 1
            x1 += 1

    else:
        y1, y2 = y2, y1

    input_message[k] = m[x1][y1]
    input_message[k + 1] = m[x2][y2]

count = 0
for i in range(len(input_message)):
    if count == 5:
        count = 0
        print(" ", end='')
    print(input_message[i], end='')
    count += 1

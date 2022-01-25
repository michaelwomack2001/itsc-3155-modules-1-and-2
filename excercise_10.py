import math
string_in = str(input('Enter a string: '))
str_length = len(string_in)

word_matrix = []
i = 0
for r in range(math.ceil(str_length/3)):
    row = []
    for col in range(3):
        if i >= str_length:
            break
        string_char = string_in[i]
        row.append(string_char)
        i += 1
        
    word_matrix.append(row)


print(word_matrix)



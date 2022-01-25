input_string = input('Enter a String: ')

lc_string = ''
up_string = ''

for i in input_string:
    if i.islower():
        lc_string += i
    elif i.isupper():
        up_string += i

combined_str = lc_string + up_string;
print(combined_str)


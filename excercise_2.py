string1 = input('Enter a string: ')
string2 = input('Enter another string: ')
is_true = True
c = 0

for i in string1:
    if i != string2[c]:
        print('False')
        is_true = False
        break
    c += 1

if(is_true):
    print('True')

